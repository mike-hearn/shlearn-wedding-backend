from django.db import models


class Invitation(models.Model):
    music_suggestions = models.TextField(max_length=1000, blank=True)
    additional_notes = models.TextField(max_length=1000, blank=True)

    class JSONAPIMeta:
        resource_name = "invitations"


    def __str__(self):
        names = ', '.join([f.__str__() for f in self.person_set.all()])
        if names:
            return "Invitation for {}".format(names)
        return "Blank invitation (#{})".format(self.id)

    @property
    def guests(self):
        return self.person_set.all()


class Person(models.Model):
    TITLE_CHOICES = (('Mr.', 'Mr.'), ('Mrs.', 'Mrs.'), ('Ms.', 'Ms.'), ('Dr.',
                                                                        'Dr.'))
    title = models.CharField(max_length=200, choices=TITLE_CHOICES, blank=True,
                             null=True)
    first_name = models.CharField(max_length=200, blank=True)
    last_name = models.CharField(max_length=200, blank=True)
    internal_name = models.CharField(max_length=200, blank=True)
    is_unknown_guest = models.BooleanField(default=False)
    attendance = models.CharField(max_length=200, blank=True)
    food_choice = models.CharField(max_length=200, blank=True)
    invitation = models.ForeignKey(
        Invitation, on_delete=models.CASCADE, blank=True, null=True)

    class JSONAPIMeta:
        resource_name = "people"

    def __str__(self):
        if self.first_name:
            return "{} {}".format(self.first_name, self.last_name)
        return self.internal_name
