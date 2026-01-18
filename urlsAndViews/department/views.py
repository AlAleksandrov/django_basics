from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request: HttpRequest, id: int) -> HttpResponse:
    return HttpResponse(f"The type is {type(id)}")

def slug_view(request: HttpRequest, slug: str) -> HttpResponse:
    return HttpResponse(f"The type is {type(slug)} and the slug is {slug}")

def path_view(request: HttpRequest, path: str) -> HttpResponse:
    return HttpResponse(f"The type is {type(path)} and the path is {path}")

def uuid_view(request: HttpRequest, uuid: str) -> HttpResponse:
    return HttpResponse(f"The type is {type(uuid)} and the uuid is {uuid}")

def show_archive(request: HttpRequest, archive_year: int) -> HttpResponse:
    return HttpResponse(f"The requested year is {archive_year}")