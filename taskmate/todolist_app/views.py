from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import TaskList
from .forms import TaskForm
from django.contrib import messages


# Create your views here.
def todolist(request):
    if request.method == "POST":
        form = TaskForm(request.POST or None)
        if form.is_valid():
            form.save()
        messages.success(request, 'New task added!')
        return redirect('todolist')
    else:
        # return HttpResponse("Welcome to todolist")
        all_tasks = TaskList.objects.all()
        context = {
            "welcome_todolist_text": "Welcome to Todolist app"
        }
        return render(request, 'todolist.html', {'all_tasks': all_tasks})


def delete_task(request, task_id):
    task = TaskList.objects.get(pk=task_id)
    task.delete()
    messages.success(request, "Your task deleted successfully!")
    return redirect('todolist')


def edit_task(request, task_id):
    task = TaskList.objects.get(pk=task_id)
    if request.method == "POST":
        form = TaskForm(request.POST or None, instance=task)
        if form.is_valid():
            form.save()
            messages.success(request, "Your task edited successfully!")
        return redirect('todolist')
    else:
        return render(request, 'edittask.html', {'task_title': task.task, 'task_status': task.status})


def complete_task(request, task_id):
    task = TaskList.objects.get(pk=task_id)
    task.status = True
    task.save()
    return redirect('todolist')

def pending_task(request, task_id):
    task = TaskList.objects.get(pk=task_id)
    task.status = False
    task.save()
    return redirect('todolist')

def contact(request):
    context = {
        "welcome_contact_text": "Welcome to Contact Us Page"
    }
    return render(request, 'contact.html', context)


def about(request):
    context = {
        "welcome_about_text": "Welcome to About Us Page"
    }
    return render(request, 'about.html', context)
