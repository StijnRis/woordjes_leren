from django.utils import timezone
import datetime
from django.db import models

# Create your models here.
class List(models.Model):
    name = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.name
    
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Question(models.Model):
    lijst = models.ForeignKey(List, on_delete=models.CASCADE)
    word = models.CharField(max_length=200)
    answer = models.CharField(max_length=200)
    tries = models.IntegerField(default=0)

    def __str__(self):
        return self.word