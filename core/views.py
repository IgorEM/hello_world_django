from django.shortcuts import render, HttpResponse

# Create your views here.

def hello(request, nome,idade):
    return HttpResponse('<h1>Hello {} - {} anos <h1>'.format(nome,idade))

def soma(request,num1,num2):
    soma = num1 + num2
    return HttpResponse('{} + {} = {}'.format(num1,num2,soma))