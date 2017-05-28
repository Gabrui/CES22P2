from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.
#This File receive client request and send back the response

def index(request):
    #return HttpResponse("<h1>This is the homepage<h1/>")
    return render(request, "templates/homepage/homepage.html")



