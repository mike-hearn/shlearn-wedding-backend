from rest_framework import viewsets

from rsvp.models import Invitation, Person
from rsvp.serializers import InvitationSerializer, PersonSerializer


class PersonViewSet(viewsets.ModelViewSet):
    resource_name = 'people'
    queryset = Person.objects.all()
    serializer_class = PersonSerializer


class InvitationViewSet(viewsets.ModelViewSet):
    resource_name = 'invitations'
    queryset = Invitation.objects.all()
    serializer_class = InvitationSerializer
