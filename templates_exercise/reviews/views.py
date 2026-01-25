from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, get_object_or_404

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