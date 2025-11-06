from django.shortcuts import render
from ToDo.models import Task
from django.shortcuts import get_object_or_404 

def home(request):
    tasks= Task.objects.filter(is_completed=False).order_by('-created_at')
    completed_tasks= Task.objects.filter(is_completed=True)
    context={
        'tasks':tasks,
        'completed_tasks':completed_tasks,
        }

    return render(request, 'home.html', context)