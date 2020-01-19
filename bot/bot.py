from .models import BotQuestionRegexModel, BotAnswerLinkModel, BotAnswerTextModel
import random


def get_bot_response(query):
    model = BotQuestionRegexModel.objects.all()
    for every_model in model:
        if every_model.regex.match(query) is not None:
            print(every_model.answer)
            if every_model.answer == 'LINK':
                return "Please refer this link: " + str(every_model.link.link)
            else:
                res = every_model.text.text.split('","')
                res = random.choice(res)
                return res
    return "You are out of our reach. Please reach us at info@thapar.edu"