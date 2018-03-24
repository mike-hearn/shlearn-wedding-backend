from django.contrib import admin

from rsvp.models import Invitation, Person


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'internal_name', 'friday', 'saturday')
    ordering = ('first_name', )

    def friday(self, obj):
        if 'Friday' in obj.attendance:
            return '✅'
        else:
            return '-'

    def saturday(self, obj):
        if 'Saturday' in obj.attendance:
            return '✅ '


class PersonInline(admin.StackedInline):
    model = Person


@admin.register(Invitation)
class InvitationAdmin(admin.ModelAdmin):
    inlines = [PersonInline]
