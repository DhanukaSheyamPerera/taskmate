from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import CustomUserRegistration

# Create your views here.
def register(request):
    if request.method == 'POST':
        register_form = CustomUserRegistration(request.POST)
        if register_form.is_valid():
            register_form.save()
            messages.success(request, 'Account created successfully! Log in to get started!')
        # else:
        #     print(register_form.errors)
        return redirect('todolist')
    else:
        register_form = CustomUserRegistration()
        return render(request, 'register.html', {"register_form": register_form})