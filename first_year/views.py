from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def first_year_students(request):
    return HttpResponse('<h1>Nukber of students in first Year are 180</h1>')
