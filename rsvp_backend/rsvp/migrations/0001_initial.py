# Generated by Django 2.0.3 on 2018-03-15 17:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Invitation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('music_suggestions', models.CharField(max_length=1000)),
                ('additional_notes', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=200)),
                ('nickname', models.CharField(max_length=200)),
                ('internal_name', models.CharField(max_length=200)),
                ('is_unknown_guest', models.BooleanField(default=False)),
                ('attendance', models.CharField(max_length=200)),
                ('food_choice', models.CharField(max_length=200)),
                ('invitation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rsvp.Invitation')),
            ],
        ),
    ]