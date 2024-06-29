from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm, EditTaskForm
from accounts.models import CustomUser
from django.db.models import Q
from datetime import datetime


def tasks(request):
    users = CustomUser.objects.all()

    selected_user = request.GET.get('user', '')
    selected_priority = request.GET.get('priority', '')
    selected_date_from = request.GET.get('date_from', '')
    selected_date_to = request.GET.get('date_to', '')
    selected_title = request.GET.get('title', '')

    filters = Q()

    if selected_user:
        filters &= Q(user_id=selected_user)

    if selected_priority:
        filters &= Q(priority=selected_priority)

    if selected_date_from:
        filters &= Q(due_date__gte=datetime.strptime(selected_date_from, '%Y-%m-%d'))

    if selected_date_to:
        filters &= Q(due_date__lte=datetime.strptime(selected_date_to, '%Y-%m-%d'))

    if selected_title:
        filters &= Q(title__icontains=selected_title)

    if request.user.is_authenticated:
        tasks = Task.objects.filter(filters)
    else:
        tasks = Task.objects.none()

    context = {
        'tasks': tasks,
        'users': users,
        'selected_user': selected_user,
        'selected_priority': selected_priority,
        'selected_date_from': selected_date_from,
        'selected_date_to': selected_date_to,
        'selected_title': selected_title,
    }

    return render(request, 'manager_task/tasks.html', context)


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
