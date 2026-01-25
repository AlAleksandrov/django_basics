from django.shortcuts import render
from datetime import datetime
from django.http import HttpRequest, HttpResponse

# Create your views here.
def current_time_view(request: HttpRequest) -> HttpResponse:
    now = datetime.now()
    context = {
        'current_time': now.strftime("%Y-%m-%d %H:%M:%S"),
        'page_title': 'Current Time',
    }
    return render(request, 'common/current_time.html', context)
