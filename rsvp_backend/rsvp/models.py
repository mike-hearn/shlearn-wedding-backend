from django.db import models


class Invitation(models.Model):
    music_suggestions = models.CharField(max_length=1000)
    additional_notes = models.CharField(max_length=1000)


class Person(models.Model):
    full_name = models.CharField(max_length=200)
    nickname = models.CharField(max_length=200)
    internal_name = models.CharField(max_length=200)
    is_unknown_guest = models.BooleanField(default=False)
    attendance = models.CharField(max_length=200)
    food_choice = models.CharField(max_length=200)
    invitation = models.ForeignKey(Invitation, on_delete=models.CASCADE)
