from django.shortcuts import render
from django.http import HttpResponse
from .models import TaskList

# Create your views here.
def todolist(request):
    # return HttpResponse("Welcome to todolist")
    all_tasks = TaskList.objects.all()
    context = {
        "welcome_todolist_text":"Welcome to Todolist app"
    }
    return render(request, 'todolist.html', {'all_tasks': all_tasks})

def contact(request):
    context = {
        "welcome_contact_text":"Welcome to Contact Us Page"
    }
    return render(request, 'contact.html', context)

def about(request):
    context = {
        "welcome_about_text":"Welcome to About Us Page"
    }
    return render(request, 'about.html', context)