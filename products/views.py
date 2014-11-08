from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse("Index")

def category(request, category, page="1"):
    return HttpResponse("Category: " + category + " Page: " + page)

def show(request, category, product):
    return HttpResponse("Category: " + category + " Product: " + product)
