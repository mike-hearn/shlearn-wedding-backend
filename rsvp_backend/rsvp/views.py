from fuzzywuzzy import process
from rest_framework import viewsets
from rest_framework.response import Response

from rsvp.models import Invitation, Person
from rsvp.serializers import InvitationSerializer, PersonSerializer


class PersonViewSet(viewsets.ModelViewSet):
    resource_name = 'people'
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

    def list(self, request, *args, **kwargs):
        if request.query_params.get('filter[fullName]'):
            name_filter = request.query_params.get('filter[fullName]')
            people_dict = {p.__str__(): p.id for p in Person.objects.all() if not p.is_unknown_guest}
            people = list(people_dict)
            name_match = process.extract(name_filter, people)[0][0]
            queryset = Person.objects.filter(id=people_dict[name_match])

        if not queryset:
            queryset = self.filter_queryset(self.get_queryset())

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
