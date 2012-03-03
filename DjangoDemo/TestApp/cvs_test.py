from TestApp.list import address

__author__ = 'yin'
#coding=utf-8
from django.http import HttpResponse
from django.template import Context
from django.template import loader

def output(request, filename):
    response = HttpResponse(mimetype='text/csv')
    response['context-description'] = 'attachment; filename=%s.csv'% filename
    print("##########")
    t = loader.get_template('cvs.html')
    c = Context({
        'data': address,
    })
    response.write(t.render(c))
    return response