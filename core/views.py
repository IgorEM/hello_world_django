from django.shortcuts import render, HttpResponse

# Create your views here.

def hello(request, nome,idade):
    return HttpResponse('<h1>Hello {} - {} anos <h1>'.format(nome,idade))

# def meusite(request):
#     return HttpResponse('Meu Primeiro Site em Django S2')