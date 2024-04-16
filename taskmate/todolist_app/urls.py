from django.urls import path
from . import views

urlpatterns = [
    path('', views.todolist, name='todolist'),
    path('delete/<task_id>', views.delete_task, name="deletetask"),
    path('edit/<task_id>', views.edit_task, name="edittask"),
    path('complete/<task_id>', views.complete_task, name="completetask"),
    path('pending/<task_id>', views.pending_task, name="pendingtask"),
    path('contact', views.contact, name='contact'),
    path('about', views.about, name='about')

]
