from django.shortcuts import render
from django.http import HttpResponse


def op(request):
    return render(request, "index.html")
