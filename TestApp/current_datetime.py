__author__ = 'yin'
from django.http import HttpResponse
import datetime

def index(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s</body></html>"% now
    return HttpResponse(html)

def hours_add(request, offset):
    print(offset)
    offset = int(offset)
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    html = "<html><body>In %s Hours, It will be %s.</body></html>"% (offset, dt)
    return HttpResponse(html)