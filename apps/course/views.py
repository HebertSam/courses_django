from django.shortcuts import render, redirect
from django.contrib import messages
from models import courses

# Create your views here.
def index(request):

    data = courses.objects.all()

    context = {
        'course_data': data
    }

    return render(request, 'course/index.html', context)

def destroy(request, id):
    data = courses.objects.get(id=id)

    context = {
        'course_data': data
    }

    return render(request, 'course/destroy.html', context)

def create(request):

    errors = courses.objects.basic_validator(request.POST)

    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
            return redirect('/')
    else:
        courses.objects.create(name=request.POST['name'], description=request.POST['description'])
        return redirect('/')

def delete(request, id):

    course = courses.objects.get(id=id)
    course.delete()
    return redirect('/')

