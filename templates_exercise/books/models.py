from django.db import models
from django.template.defaultfilters import slugify

from books.validators import range_validator2, RangeValidator
from common.models import TimeStampModel


# Create your models here.
class Book(TimeStampModel):
    class GenreChoices(models.TextChoices):
        FICTION = 'Fiction', 'Fiction'
        NON_FICTION = 'Non-Fiction', 'Non-Fiction'
        SCIENCE = 'Science', 'Science'
        FANTASY = 'Fantasy', 'Fantasy'
        HISTORY = 'History', 'History'
        MISTERY = 'Mistery', 'Mistery'


    title = models.CharField(
        max_length=100,
        unique=True,
    )
    price = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        validators=[
            # range_validator2(0, 1000),
            RangeValidator(0, 1000, message='Price should be between 0 and 1000'),
        ],
    )
    isbn = models.CharField(
        max_length=12,
        unique=True,
    )
    cover_image = models.ImageField(
        null=True,
        blank=True,
        upload_to='book_covers/',
    )
    author = models.CharField(
        max_length=100,
        null=True,
        blank=True,
    )
    genre = models.CharField(
        max_length=50,
        choices=GenreChoices.choices,
    )
    publishing_date = models.DateField()
    description = models.TextField()
    image_url = models.URLField()
    slug = models.SlugField(
        max_length=100,
        unique=True,
        blank=True,
    )
    pages = models.PositiveIntegerField(
        null=True,
        blank=True,
    )
    publisher = models.CharField(
        max_length=100,
    )
    tags = models.ManyToManyField(
        'Tag',
        blank=True,
        related_name='books',
    )

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f'{self.title}-{self.publisher}')
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class Tag(models.Model):
    name = models.CharField(
        max_length=50,
    )

    def __str__(self) -> str:
        return self.name