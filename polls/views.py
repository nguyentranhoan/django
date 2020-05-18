from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Choice, Question, Result, User
from rest_framework import viewsets
from .serializers import QuestionSerializer, UserSerializer
from rest_framework import status
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from . import serializers
from . import models
from .serializers import ChoiceSerializer
from rest_framework.authtoken.models import Token
# from django.contrib.auth.models import User


@csrf_exempt
@api_view(['POST'])
def login(request):
    username = request.data.get("username")
    password = request.data.get("password")
    # print(username, "\n", password)
    info = User.objects.filter(first_name=username,last_name=password).first()
    if info is None:
        return Response({"message": "user does not exist!"})
    else:
        return Response(info.id)


class QuestionViewSet(viewsets.ModelViewSet):
    # queryset = Result.objects.raw("""select
    #                                     polls_question.question_text,
    #                                     polls_question.id,
    #                                     result.point
    #                                 from
    #                                     result join polls_question
    #                                     on result.question_id = polls_question.id
    #                                 where
    #                                     polls_question.id =1""")
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    # qr = Result.objects.raw("select * from result join question on result.question = question.id where question.id =1")


@api_view(['GET'])
def home(request):
    return Response({"message": "Welcome home"},
                    status=status.HTTP_200_OK)


class QuestionListCreateAPIView(APIView):

    def get(self, request):
        articles = models.Question.objects.all()
        serializer = serializers.QuestionSerializer(articles, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = serializers.QuestionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ChoiceList(generics.ListCreateAPIView):
    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer


class ChoiceDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer


class Login(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
