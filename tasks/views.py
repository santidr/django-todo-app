from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import Task
from .forms import TaskForm

# Create your views here.
def index(request):
    tasks = Task.objects.all()
    form = TaskForm()

    if request.method == 'POST':
        form = TaskForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'tasks_list': tasks, 'form': form}
    return render(request, 'tasks/tasks_list.html', context)

def task_update_view(request, pk):
    task = Task.objects.get(id=pk)
    form = TaskForm(instance=task)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)

        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form': form}
    return render(request, 'tasks/task_edit.html', context)

def task_delete_view(request, pk):
    task = Task.objects.get(id=pk)

    if request.method == 'POST':
        task.delete()
        return redirect('home')

    context = {'item': task}
    return render(request, 'tasks/task_delete.html', context)

def cross_out_item_view(request, pk):
    task = Task.objects.get(id=pk)
    task.completed = True
    task.save()
    return redirect('home')

def uncross_item_view(request, pk):
    task = Task.objects.get(id=pk)
    task.completed = False
    task.save()
    return redirect('home')