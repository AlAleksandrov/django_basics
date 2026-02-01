from django.db.models import Avg
from django.http import HttpResponse, HttpRequest
from django.shortcuts import render, get_object_or_404, redirect
from books.forms import BookFormBasic, BookCreateForm, BookEditForm, BookDeleteForm
from books.models import Book


# Create your views here.
def landing_page(request: HttpRequest) -> HttpResponse:
    total_books = Book.objects.count()
    latest_books = Book.objects.order_by('-publishing_date').first()

    context = {
        'total_books': total_books,
        'latest_books': latest_books,
        'page_title': 'Home',
    }

    return render(request, 'books/landing_page.html', context)

def book_list(request: HttpRequest) -> HttpResponse:
    list_books = Book.objects.annotate(
        avg_rating=Avg('reviews__rating')
    ).order_by('title')

    context = {
        'books': list_books,
        'page_title': 'Dashboard',
    }

    return render(request, 'books/list.html', context)

def book_details(request: HttpRequest, slug: str) -> HttpResponse:
    book = get_object_or_404(
        Book.objects.annotate(
            avg_rating=Avg('reviews__rating'),
        ),
        slug=slug,
    )

    context = {
        'book': book,
        'page_title': f'{book.title} details',
    }

    return render(request, 'books/detail.html', context)

def book_create(request: HttpRequest) -> HttpResponse:
    form = BookCreateForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        form.save()

        # # for forms.Form
        # Book.objects.create(
        #     # title=form.cleaned_data['title'],
        #     # price=form.cleaned_data['price'],
        #     # isbn=form.cleaned_data['isbn'],
        #     # genre=form.cleaned_data['genre'],
        #     # publishing_date=form.cleaned_data['publishing_date'],
        #     # description=form.cleaned_data['description'],
        #     # image_url=form.cleaned_data['image_url'],
        #     # publisher=form.cleaned_data['publisher'],
        #     **form.cleaned_data
        # )
        return redirect('books:Home')

    context = {
        'form': form,
    }

    return render(request, 'books/create.html', context)

def book_edit(request: HttpRequest, pk: int) -> HttpResponse:
    book = get_object_or_404(Book, pk=pk)
    form = BookEditForm(request.POST or None, instance=book)

    if request.method == 'POST' and form.is_valid():
        form.save()

        return redirect('books:Home')

    context = {
        'form': form,
    }

    return render(request, 'books/edit.html', context)

def book_delete(request: HttpRequest, pk: int) -> HttpResponse:
    book = get_object_or_404(Book, pk=pk)
    form = BookDeleteForm(request.POST or None, instance=book)

    if request.method == 'POST' and form.is_valid():
        book.delete()

        return redirect('books:Home')

    context = {
        'form': form,
    }

    return render(request, 'books/delete.html', context)