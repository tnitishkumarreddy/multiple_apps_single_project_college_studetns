from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def third_year_students(request):
    return HttpResponse('<h1>Number of students in third year are 173</h1>')