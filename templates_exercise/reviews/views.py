from django.forms import modelformset_factory
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from books.models import Book
from reviews.forms import ReviewCreateForm, ReviewEditForm, ReviewDeleteForm
from reviews.models import Review


# Create your views here.
def recent_reviews(request: HttpRequest) -> HttpResponse:
    DEFAULT_REVIEWS_COUNT = 5
    reviews_count = int(request.GET.get('count', DEFAULT_REVIEWS_COUNT))
    reviews = Review.objects.select_related('book')[:reviews_count]

    context = {
        'reviews': reviews,
        'page_title': 'Recent reviews',
    }

    return render(request, 'reviews/list.html', context)

def review_details(request: HttpRequest, pk: int) -> HttpResponse:
    review = get_object_or_404(
        Review.objects.select_related('book'),
        pk=pk,
    )

    # Prepare star rating HTML without using Django filters in the template
    star_rating_html = ""
    full_stars = int(review.rating)
    has_half_star = (review.rating - full_stars) >= 0.5

    for _ in range(full_stars):
        star_rating_html += '<i class="bi bi-star-fill text-warning"></i>'
    if has_half_star:
        star_rating_html += '<i class="bi bi-star-half text-warning"></i>'
    for _ in range(5 - full_stars - (1 if has_half_star else 0)):
        star_rating_html += '<i class="bi bi-star text-warning"></i>'

    context = {
        'review': review,
        'page_title': f'{review.author}\'s review on {review.book.title}',
        'star_rating_html': star_rating_html,
    }

    return render(request, 'reviews/detail.html', context)

def review_create(request: HttpRequest, pk: int) -> HttpResponse:
    book = get_object_or_404(Book, pk=pk)
    form = ReviewCreateForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        review = form.save(commit=False)
        review.book = book
        review.save()
        return redirect('books:details', slug=book.slug)

    context = {
        'form': form,
        'book': book,
    }

    return render(request, 'reviews/create.html', context)

def review_bulk_edit(request: HttpRequest, book_slug: str) -> HttpResponse:
    book = get_object_or_404(Book, slug=book_slug)
    ReviewFormSet = modelformset_factory(
        Review,
        form=ReviewEditForm,
        can_delete=True,
        extra=1,
    )

    formset = ReviewFormSet(
        request.POST or None,
        queryset=Review.objects.filter(book=book),
        form_kwargs={'book': book},
    )

    if request.method == 'POST' and formset.is_valid():
        instances = formset.save(commit=False)

        for instance in instances:
            instance.book = book
            instance.save()

        for instance in formset.deleted_objects:
            instance.delete()


        return redirect('review:list')

    context = {
        'formset': formset,
        'book': book,
    }

    return render(request, 'reviews/formset_edit.html', context)

def review_edit(request: HttpRequest, pk: int) -> HttpResponse:
    review = get_object_or_404(Review, pk=pk)
    form = ReviewEditForm(request.POST or None, instance=review)

    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('books:details', slug=review.book.slug)

    context = {
        'form': form,
        'review': review,
    }

    return render(request, 'reviews/edit.html', context)

def review_delete(request: HttpRequest, pk: int) -> HttpResponse:
    review = get_object_or_404(Review, pk=pk)
    form = ReviewDeleteForm(request.POST or None, instance=review)

    if request.method == 'POST' and form.is_valid():
        review.delete()
        return redirect('books:details', slug=review.book.slug)

    context = {
        'form': form,
        'review': review,
    }

    return render(request, 'reviews/delete.html', context)