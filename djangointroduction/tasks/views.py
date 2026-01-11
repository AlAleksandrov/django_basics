from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from tasks.models import Task


def index(request: HttpRequest) -> HttpResponse:

    context = {
        'tasks': Task.objects.all(),
    }

    return render(request, 'index.html', context, content_type='text/html; charset=utf-8')


def index2(request: HttpRequest) -> HttpResponse:
    all_tasks = Task.objects.all()

    template = [
        '<h1>All tasks</h1>' if all_tasks else '<h1>No tasks</h1>',
        *[f"<li>{t.title} - {t.is_completed}</li>" for t in all_tasks],
    ]

    return HttpResponse(
        '\n'.join(template),
    )
