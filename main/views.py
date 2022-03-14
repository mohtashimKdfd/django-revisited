from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from django.http import JsonResponse
from django.contrib.auth.hashers import make_password, check_password
from rest_framework import parsers

#models
from main.models import Users

#serializers

from main.serializers import UsersSerializer


#for logging
from loguru import logger
import loguru

loguru.logger.add(
    "loguru.log",
    level="INFO",
    format="{time} {level} {message}",
    retention='1 minute',
)
loguru.logger.info('Loguru is up and running')




class HomeView(APIView):

    def get(self, request):
        logger.info('Home page: {}'.format(request.method),request)
        return HttpResponse("<h1>Helllooooo boisss and grillls</h1>")


class UsersView(APIView):
    parser_classes = (parsers.JSONParser,)
    def get(self, request):
        logger.info('Users page: {}'.format(request.method),request)
        allUsers = Users.objects.all()
        serialized = UsersSerializer(allUsers,many=True)
        return JsonResponse(serialized.data,safe=False)
    
    def post(self, request):
        logger.info('Home page: {}'.format(request.method),request)
        print(request.data)
        username = request.data.get('username')
        password = make_password(request.data.get('password'))
        newUser = Users(username=username,password=password)
        newUser.save()
        serilized = UsersSerializer(newUser)
        return JsonResponse(serilized.data,safe=False)