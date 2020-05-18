from rest_framework import serializers
from .models import Question, Choice, Result, User


class ResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = Result
        fields = ['point']


class ChoiceSerializer(serializers.ModelSerializer):
    choice_result = ResultSerializer(many=True, read_only=True)

    class Meta:
        model = Choice
        fields = ['id', 'question', 'choice_text', 'votes', 'choice_result']


class QuestionSerializer(serializers.HyperlinkedModelSerializer):
    choices = ChoiceSerializer(many=True, read_only=True)
    queryset = Result.objects.all()
    # question_result = ResultSerializer(queryset, many=True, read_only=True)

    class Meta:
        model = Question
        fields = ['id', 'question_text', 'pub_date', 'choices']


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['first_name', 'last_name']
