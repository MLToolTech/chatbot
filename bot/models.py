from django.db import models
from django.contrib.auth.models import User
from regex_field.fields import RegexField
import re
from .choices import ANSWER_CHOICES


class BotModel(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=200)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name + ' created by ' + self.created_by.username


class BotAnswerLinkModel(models.Model):
    bot = models.ForeignKey(BotModel, on_delete=models.CASCADE)
    link = models.URLField()

    def __str__(self):
        return str(self.link) + ' added by ' + self.bot.created_by.username


class BotAnswerTextModel(models.Model):
    bot = models.ForeignKey(BotModel, on_delete=models.CASCADE)
    text = models.CharField(max_length=200)

    def __str__(self):
        return str(self.text) + ' added by ' + self.bot.created_by.username


class BotQuestionRegexModel(models.Model):
    regex = RegexField(max_length=500, re_flags=re.IGNORECASE)
    answer = models.CharField(max_length=100, choices=ANSWER_CHOICES)
    link = models.ForeignKey(BotAnswerLinkModel, null=True, blank=True, on_delete=models.CASCADE)
    text = models.ForeignKey(BotAnswerTextModel, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.regex)


class ChatTransactionModel(models.Model):
    query = models.CharField(max_length=1000)
    response = models.CharField(max_length=500)
