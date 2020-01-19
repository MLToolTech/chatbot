from django.contrib import admin
from bot.models import BotModel, BotQuestionRegexModel, BotAnswerLinkModel, BotAnswerTextModel


admin.site.register(BotModel)
admin.site.register(BotQuestionRegexModel)
admin.site.register(BotAnswerLinkModel)
admin.site.register(BotAnswerTextModel)
