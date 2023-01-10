from django.http import HttpResponse, JsonResponse
from django.shortcuts import render


# Create your views here.
def home(request):
    if request.method == 'GET':
        print('get method')
        return HttpResponse('get method')

    if request.method == 'POST':
        pass
