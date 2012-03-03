__author__ = 'yin'
from models import Book
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.http import Http404
import datetime

def latest_books(request):
    book_list = Book.objects.order_by('-pub_date')[:10]
    return render_to_response('latest_books.html', {'book_list':book_list})

def hello(request):
    return HttpResponse("hello world")

def current_time(request):
    now = datetime.datetime.now()
    html = "now is %s" % now
    return HttpResponse(html)

def hours_plus(request, offset):
    raise Http404()
    offset = int(offset)
    now = datetime.datetime.now() + datetime.timedelta(hours=offset)
    html = "after %s hours ,time is %s" % (offset, now)
    return HttpResponse(html)