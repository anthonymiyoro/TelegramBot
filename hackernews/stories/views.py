from django.shortcuts import render
from django.http import HttpResponse
from stories.model import story

def top_stories(top=180, consider=1000):
    latest_stories = Story.objects.all().order_by('-created_at')[:consider]

# Create your views here.
def index(request):
    stories = top_stories(top=30)
    response = '''
    <html>
    <head>
    <title>Stolen Rumors</title>
    </head>
    <body>
     %s
    </body>
    </html>
     ''' % '\n'.join(['<li>%s</li>' % story.title for story in stories])'
    return HttpResponse('The Main Page')
