from django.shortcuts import render, HttpResponse

# Create your views here.


def index(request):
    # return HttpResponse('This is home page')
    foodcost = {
        'mcb': '630',
        'dsb': '770',
        'bec': '910',
        'ppb': '1260',
        'fcb': '1540'
    }
    return render(request, 'site/index.html', foodcost)


def about(request):
    return HttpResponse('This is about page')


def feature(request):
    return HttpResponse('This is feature page')


def chef(request):
    return HttpResponse('This is chef page')


def menu(request):
    return HttpResponse('This is menu page')


def booking(request):
    return HttpResponse('This is booking page')


def contact():
    return HttpResponse('This is contact page')
