from pyexpat import model
from statistics import mode
from django.db import models

# Create your models here.

class Meeting(models.Model):
    TYPE_OF_CONTACT = [
        ('contact', '대면'),
        ('untact', '비대면'),
    ]
    
    meetingDate = models.DateField()
    location = models.CharField(max_length=20)
    visitor = models.CharField(max_length=20)
    manager = models.CharField(max_length=20)
    contact = models.CharField(max_length=10, choices=TYPE_OF_CONTACT)
    comment = models.TextField(max_length=100)
    
class Reply(models.Model):
    meeting = models.ForeignKey(Meeting, on_delete=models.CASCADE)
    user = models.CharField(max_length=10)
    date = models.DateField()
    content = models.TextField(max_length=100)
    
