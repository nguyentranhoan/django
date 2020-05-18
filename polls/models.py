# Create your models here.

from django.db import models
from django.utils import timezone


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.question_text

    def hello(self):
        return f"{self.question_text} was published at {self.pub_date}"


class Choice(models.Model):
    question = models.ForeignKey(Question, related_name='choices', on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text


class User(models.Model):
    class Meta:
        db_table = 'user'

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    # def __str__(self):
    #     return f"{self.first_name} {self.last_name}"


class Result(models.Model):
    class Meta:
        db_table = 'result'

    question = models.ForeignKey(Question, related_name='question_result', on_delete=models.CASCADE)
    choice = models.ForeignKey(Choice, related_name='choice_result', on_delete=models.CASCADE)
    point = models.IntegerField()
