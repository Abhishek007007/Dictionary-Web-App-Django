from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

# Create your views here.


def home(request: HttpRequest) -> HttpResponse:
    """Returns the contents of home page"""
    return render(request, "index.html")
