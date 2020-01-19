from rest_framework import serializers
from .models import ChatTransactionModel
from .bot import get_bot_response


class ChatTransactionSerializer(serializers.ModelSerializer):
    query = serializers.CharField()
    response = serializers.HiddenField(default='')

    def create(self, validated_data):
        validated_data['response'] = get_bot_response(validated_data['query'])
        return super().create(validated_data)

    def to_representation(self, instance):
       response_dict = {
           'query': instance.query,
           'response': instance.response
       }
       return response_dict

    class Meta:
        model = ChatTransactionModel
        fields = '__all__'
