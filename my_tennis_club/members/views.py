from django.shortcuts import render
from django.http import HttpResponse

def members(request):
    return HttpResponse("<h2>Lets go IT242!</h2>")
