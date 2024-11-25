from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def fourth_year_students(request):
    return HttpResponse('<h1>Number of students in fourth year are 169</h1>')