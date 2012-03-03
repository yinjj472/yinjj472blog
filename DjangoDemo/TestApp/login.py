__author__ = 'yin'
#coding=utf-8
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect

def login(request):
    username = request.POST.get('username', None)
    if username:
        request.session['username'] = username
    username = request.session.get('username', None)
    if username:
        return render_to_response('login.html', {'username':username})
    else:
        return render_to_response('login.html')

def logout(request):
    try:
        del request.session['username']
    except keyError:
        pass
    return HttpResponseRedirect("/login/")