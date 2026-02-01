from typing import Any
from django import forms
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

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        self.fields['tags'].queryset = Tag.objects.all()


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