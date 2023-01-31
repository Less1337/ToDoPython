from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods


# Create your views here.
from .models import Task
from django.db.models import Q

def index(request):
    search = request.GET.get('search', '')
    if search:
        tasks = Task.objects.filter(Q(title__icontains=search) | Q(content__icontains=search))
    else:
        tasks = Task.objects.all()

    return render(request, 'todoapp/index.html', {'tasks': tasks, 'title': 'Главная страница'})

#def task(request, taskid, title):
#    return HttpResponse(f"<h1>task</h1><p>{taskid}</p>")



def pageNotFound(request, exception):
    return HttpResponseNotFound('Page not found')


@require_http_methods(['POST'])
@csrf_exempt
def addtask(request):
    title = request.POST['title']
    content = request.POST['content']
    task = Task(title=title, content=content)
    task.save()
    return redirect('index')


def complete(request, task_id):
    task = Task.objects.get(id=task_id)
    task.is_done = not task.is_done
    task.save()
    return redirect('index')


def delete (request, task_id):
    task = Task.objects.get(id=task_id)
    task.delete()
    return redirect('index')