from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    stories = top_stories(top=30)
    response = ''
    return HttpResponse('The Main Page')
