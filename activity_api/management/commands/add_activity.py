from django.core.management.base import BaseCommand, CommandError
from activity_api.models import *
from datetime import datetime
from random import randint
from faker import Faker

class Command(BaseCommand):

    help = 'Generates and adds dummy data to the database'

    def handle(self, *args, **options):

        fake_generator = Faker()

        # users = User.objects.all()
        # for u in users:
        #     u.delete()
        
        for _ in range(3):
            
            first_name = fake_generator.first_name()
            last_name  = fake_generator.last_name()
            tz         = fake_generator.timezone()

            activity_periods = {"start_time": [], "end_time": []}

            day   = randint(1, 30)
            month = 6
            year  = 2020

            for _ in range(3):

                hour   = randint(0, 23)
                minute = randint(0, 39)
                second = randint(0, 39)

                activity_periods["start_time"].append(datetime(year, month, day, hour, minute, second))
                activity_periods["end_time"].append(datetime(year, month, day, hour, minute + 20, second + 20))

            u = User(first_name=first_name, last_name=last_name, tz=tz)
            u.save()

            for st, et in zip(activity_periods["start_time"], activity_periods["end_time"]):
                
                ap = ActivityPeriod(start_time=st, end_time=et, user=u)
                ap.save()

            self.stdout.write(self.style.SUCCESS('Successfully added user "%s %s"' % (first_name, last_name)))
