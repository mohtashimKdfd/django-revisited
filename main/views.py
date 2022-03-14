from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView

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
