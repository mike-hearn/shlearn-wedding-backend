from django.contrib import admin

from rsvp.models import Invitation, Person


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    pass


class PersonInline(admin.StackedInline):
    model = Person


@admin.register(Invitation)
class InvitationAdmin(admin.ModelAdmin):
    inlines = [PersonInline]
