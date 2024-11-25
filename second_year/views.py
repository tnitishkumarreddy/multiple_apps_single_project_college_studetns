from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def second_year_students(request):
    return HttpResponse('<h1>Number of students in second year are 162</h1>')
