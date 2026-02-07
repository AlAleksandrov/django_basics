from typing import Any

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django import forms
from django.core.exceptions import ValidationError

from books.models import Book, Tag
from common.forms import DisabledFieldsMixin


# class BookFormBasic(forms.Form):
#     title = forms.CharField(
#         max_length=100,
#         widget=forms.TextInput(attrs={'placeholder': 'e.g. Done'})
#     )
#     price = forms.DecimalField(
#         max_digits=6,
#         decimal_places=2,
#         min_value=0,
#         label='Price (USD)',
#         widget=forms.NumberInput(attrs={'placeholder': 'e.g. 10.00', 'step': '0.1'}),
#     )
#
#     isbn = forms.CharField(
#         max_length=12,
#         min_length=10,
#         widget=forms.TextInput(attrs={'placeholder': 'e.g. 123456789012', 'pattern': '[0-9]{12}'}),
#     )
#
#     genre = forms.ChoiceField(
#         choices=Book.GenreChoices.choices,
#         widget=forms.Select(attrs={'class': 'form-select', 'aria-label': 'Default select example', 'required': True, }),
#     )
#
#     publishing_date = forms.DateField(
#         initial=date.today,
#         widget=forms.DateInput(attrs={'type': 'date'}),
#     )
#
#     description = forms.CharField(
#         widget=forms.Textarea(attrs={'rows': 4, 'placeholder': 'e.g. This is a great book!'}),
#     )
#
#     image_url = forms.URLField(
#         widget=forms.URLInput(attrs={'placeholder': 'e.g. https://example.com/image.jpg'}),
#     )
#
#     publisher = forms.CharField(
#         max_length=100,
#         widget=forms.TextInput(attrs={'placeholder': 'e.g. John Doe'}),
#     )

class BookFormBasic(forms.ModelForm):
    field_order = ['title', 'price', 'isbn', 'genre', 'publishing_date', 'description', 'image_url', 'publisher', 'tags']

    class Meta:
        model = Book
        exclude = ['slug']

        error_messages = {
            'title': {
                'max_length': 'The title is too long, no one is going to read that'
            },
            'isbn': {
                'invalid': 'ISBN must be 12 digits long.'
            },
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-exampleForm'
        self.helper.form_class = 'blueForms'
        self.helper.form_method = 'post'

        self.helper.add_input(Submit('submit', 'Submit'))
        self.fields['tags'].queryset = Tag.objects.all()

    def clean_isbn(self) -> None:
        isbn = self.cleaned_data.get('isbn')

        if isbn.startswith("978"):
            raise forms.ValidationError('ISBN cannot start with 978')

        if isbn and len(isbn) != 12:
            raise forms.ValidationError('ISBN must be 12 digits long.')

        return isbn

    def clean(self) -> dict[str, Any]:
        cleaned = super().clean()

        genre = cleaned.get('genre')
        pages = cleaned.get('pages')

        if pages < 10 and genre == Book.GenreChoices.FICTION:
            raise ValidationError(f'Book of tipe {Book.GenreChoices.FICTION} must have at least 10 pages.')

        return cleaned

    def save(self, commit: bool = True) -> Any:
        publisher = self.cleaned_data.get('publisher')
        if publisher:
            self.instance.publisher = publisher.capitalize()

        return super().save(commit=commit)

class BookCreateForm(BookFormBasic):
    ...

class BookEditForm(BookFormBasic):
    ...

class BookDeleteForm(DisabledFieldsMixin, BookFormBasic):
    ...

class BookSearchForm(forms.Form):
    query = forms.CharField(
        max_length=100,
        label='',
        widget=forms.TextInput(attrs={'placeholder': 'Search books...'}),
        required=False
    )