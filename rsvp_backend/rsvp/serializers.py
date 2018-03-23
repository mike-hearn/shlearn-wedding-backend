from rest_framework_json_api import serializers
from rest_framework_json_api.relations import ResourceRelatedField

from rsvp.models import Invitation, Person


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ('id', 'title', 'first_name', 'last_name', 'is_unknown_guest',
                  'is_plus_one', 'attendance', 'food_choice', 'invitation')

    class JSONAPIMeta:
        included_resources = ['invitation']

class InvitationSerializer(serializers.ModelSerializer):
    guests = PersonSerializer(many=True)

    class Meta:
        model = Invitation
        fields = ('id', 'music_suggestions', 'additional_notes', 'guests')

    class JSONAPIMeta:
        included_resources = ['guests']


PersonSerializer.included_serializers = {'invitation': InvitationSerializer}
InvitationSerializer.included_serializers = {'guests': PersonSerializer}
