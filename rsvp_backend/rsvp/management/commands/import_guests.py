import csv

from django.core.management.base import BaseCommand, CommandError

from rsvp.models import Invitation, Person


class Command(BaseCommand):
    help = 'Imports and creates people & invitations from a CSV'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str)

    def clean_data(self, data):
        data = [d for d in data if 'Guest Name' not in d[0]]
        for index, item in enumerate(data):
            if item[1].strip() == '---':
                data[index][1] = None
        return data

    def handle(self, *args, **options):

        name_array = []

        with open(options['csv_file']) as csvfile:
            csvdata = csv.reader(csvfile, delimiter=',')
            for row in csvdata:
                if ([i for i in row[:2] if i]):
                    name_array.append(row[:2])

        name_array = self.clean_data(name_array)

        for invite_names in name_array:
            invitation = Invitation()
            invitation.save()

            p1_first_name = invite_names[0].split(' ')[0]
            p1_last_name = ' '.join(invite_names[0].split(' ')[1:])
            p1 = Person(
                first_name=p1_first_name,
                last_name=p1_last_name,
                invitation=invitation)
            p1.save()

            if invite_names[1]:
                if "Guest" in invite_names[1]:
                    p2 = Person(
                        is_unknown_guest=True,
                        internal_name="Guest for {}".format(invite_names[0]))
                    p2.save()
                else:
                    p2_first_name = invite_names[1].split(' ')[0]
                    p2_last_name = ' '.join(invite_names[1].split(' ')[1:])
                    p2 = Person(
                        first_name=p2_first_name,
                        last_name=p2_last_name,
                        invitation=invitation)
                p2.save()

        self.stdout.write(self.style.SUCCESS(name_array))
