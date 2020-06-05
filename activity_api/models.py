from django.db import models
from django.utils import timezone

class User(models.Model):

    first_name = models.CharField(max_length=30)
    last_name  = models.CharField(max_length=30)
    tz         = models.CharField(max_length=30)
    date_added = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return "{} {} - {}".format(self.first_name, self.last_name, self.tz) 

class ActivityPeriod(models.Model):
    
    start_time = models.DateTimeField()
    end_time   = models.DateTimeField()
    user       = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return "{} {} {}".format(self.user, self.start_time, self.end_time)
