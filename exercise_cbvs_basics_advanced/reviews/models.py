from django.core.exceptions import ValidationError
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from travelers.models import Traveler
from destinations.models import Destination


class Review(models.Model):
    class ReviewTypeChoices(models.TextChoices):
        TEXT = "Text", "Text"
        VIDEO = "Video", "Video"
        AUDIO = "Audio", "Audio"

    body = models.TextField()
    rating = models.DecimalField(
        max_digits=4,
        decimal_places=2,
        validators=[
            MinValueValidator(0.00),
            MaxValueValidator(5.00)
        ]
    )
    is_verified = models.BooleanField(
        default=False
    )
    review_type = models.CharField(
        max_length=10,
        choices=ReviewTypeChoices.choices
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    traveler = models.ForeignKey(
        Traveler,
        on_delete=models.CASCADE,
        related_name='reviews'
    )
    destination = models.ForeignKey(
        Destination,
        on_delete=models.CASCADE,
        related_name='reviews'
    )

    def clean(self) -> None:
        if self.destination_id and self.destination.is_available:
            raise ValidationError("Cannot create a review for an unavailable destination.")
        return super().clean()

    def __str__(self):
        return f"Review for {self.destination.name} by {self.traveler.name}"