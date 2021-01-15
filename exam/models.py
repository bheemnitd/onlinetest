from django.db import models
# from django.contrib.auth.models import User

# Create your models here.

ANSWER_CHOICES = ( 
("1", "option1"),
("2", "option2"),
("3", "option3"),
("4", "option4"))


    
class MultipleChoice(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.TextField(null=False)
    option1 = models.CharField(max_length=100, null=False)
    option2 = models.CharField(max_length=100, null=False)
    option3 = models.CharField(max_length=100, null=False)
    option4 = models.CharField(max_length=100, null=False)
    submitted_answer = models.CharField(max_length=100, choices=ANSWER_CHOICES, blank=True)
    correct_answer  = models.CharField(max_length=100, choices=ANSWER_CHOICES, blank=False)

class ShortAns(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.TextField(null=False)
    submitted_answer = models.TextField(blank=True)
    correct_answer  = models.TextField(blank=False)

class ImageAns(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ImageField(upload_to=None, null=True)
    submitted_answer = models.TextField(blank=True)
    correct_answer  = models.TextField(blank=False)
