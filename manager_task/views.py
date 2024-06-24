from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm, EditTaskForm
from accounts.models import CustomUser


def tasks(request):
    selected_priority = request.GET.get('priority', '')

    if selected_priority:
        tasks = Task.objects.filter(user=request.user, priority=selected_priority)
    else:
        tasks = Task.objects.filter(user=request.user)

    return render(request, 'manager_task/tasks.html', {'tasks': tasks, 'selected_priority': selected_priority})


def create_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect('tasks')
    else:
        form = TaskForm()

    return render(request, 'manager_task/create_task.html', {'form': form})


def delete_task(request, task_id):
    try:
        task_to_delete = Task.objects.get(id=task_id, user=request.user)
        task_to_delete.delete()
    except Task.DoesNotExist:
        pass

    return redirect('tasks')


def edit_task(request, task_id):
    try:
        task = Task.objects.get(id=task_id, user=request.user)
    except Task.DoesNotExist:
        return redirect('tasks')

    if request.method == 'POST':
        form = EditTaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('tasks')
    else:
        form = EditTaskForm(instance=task)

    return render(request, 'manager_task/edit_task.html', {'form': form})

