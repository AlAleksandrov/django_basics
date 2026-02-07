from django import forms
from .models import Review
from common.forms import DisabledFieldsMixin

class ReviewFormBasic(forms.ModelForm):
    class Meta:
        model = Review
        exclude = ['book']

class ReviewCreateForm(ReviewFormBasic):
    pass

class ReviewEditForm(ReviewFormBasic):
    def __init__(self, book=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.book = book

    def save(self, commit: bool = True) -> Review:
        if commit:
            self.instance.save()

        return self.instance


class ReviewDeleteForm(DisabledFieldsMixin, ReviewFormBasic):
    pass
