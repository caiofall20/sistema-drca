from django.shortcuts import render
from django.http.response import HttpResponse

def artigo(request,ano):
	return HttpResponse('Ola mundo, Esse e o ano de:  '+ano)
