from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader
from.models import Student

def students(request):
    students=Student.objects.all().values()
    template=loader.get_template('all_students.html')
    context={
        'students':students
    }
    return HttpResponse(template.render(context,request))
def details(request,id):
    student=Student.objects.get(id=id)
    template=loader.get_template('details.html')
    context={
        'students':student
    }
    
    return HttpResponse(template.render(context,request))

def main(request):
    template=loader.get_template('main.html')
    return HttpResponse(template.render())