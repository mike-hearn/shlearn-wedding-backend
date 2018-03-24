from django.conf import settings
from django.core.management import call_command
from django.db.models import Q
from django.http import HttpResponse, HttpResponseNotFound

from fuzzywuzzy.fuzz import ratio
from fuzzywuzzy.process import extract
from rest_framework import viewsets
from rest_framework.response import Response
from rsvp.models import Invitation, Person
from rsvp.serializers import InvitationSerializer, PersonSerializer


class PersonViewSet(viewsets.ModelViewSet):
    resource_name = 'people'
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

    def list(self, request, *args, **kwargs):
        """
        Override base class `list` method to filter against a provided name.
        If the name filter results in two names matching within 10 points
        (based on fuzzywuzzy's process.extract method), it returns both names.
        If only one name is found to match, we check the fuzz.ratio of the name
        against the match - the ratio is about 70, we return a positive
        (single) match. Below 70, and no person object is returned.
        """
        if request.query_params.get('filter[fullName]'):
            name_filter = request.query_params.get('filter[fullName]')

            # List of all guests who are non-plus-ones
            people_dict = {
                p.__str__(): p.id
                for p in Person.objects.all() if not p.is_plus_one
            }
            people = list(people_dict)
            match_list = extract(name_filter, people)

            # If top two matched names are similar enough (within a match
            # rating of 10), we return both names and have the user pick the
            # correct one.
            if match_list[0][1] - match_list[1][1] < 10:

                # Using extract() above, it just returns the best two name
                # matches, but both those matches don't necessarily have to be
                # *close* matches (if every other match is even worse, for
                # example).
                #
                # So if we have two names that match closely with each other,
                # but both are bad matches to the original, we don't want to
                # return either of them. We check here if the best name match
                # has an over 70% accuracy ratio with the `name_filter`. If it
                # doesn't, we return nothing. We transform everything to
                # lower() because the ratio method cares about case, and we
                # don't.
                if ratio(name_filter.lower(), match_list[0][0].lower()) > 70:
                    queryset = Person.objects.filter(
                        Q(id=people_dict[match_list[0][0]])
                        | Q(id=people_dict[match_list[1][0]]))
                else:
                    queryset = Person.objects.none()
            else:
                # Return the queryset filtered to a single person, but only if
                # the filtered name matches the returned name with a greater
                # than 70% degree of accuracy.
                queryset = Person.objects.filter(
                    id=people_dict[match_list[0][0]]) if ratio(
                        name_filter.lower(), match_list[0][0]
                        .lower()) > 70 else Person.objects.none()

        try:
            queryset
        except NameError:
            queryset = self.filter_queryset(self.get_queryset())

        # Boilerplate code taken from parent's list method
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class InvitationViewSet(viewsets.ModelViewSet):
    resource_name = 'invitations'
    queryset = Invitation.objects.all()
    serializer_class = InvitationSerializer


def reset_database(request):
    """View intended to be used for testing only. Resets the database to a
    consistent state."""
    if settings.DEBUG:
        call_command("flush", "--no-input")
        call_command("loaddata", "guests")
        return HttpResponse("<h1>Database reset to base state.</h1>")
    else:
        return HttpResponseNotFound()
