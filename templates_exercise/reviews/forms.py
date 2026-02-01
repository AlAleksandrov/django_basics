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
    pass

class ReviewDeleteForm(DisabledFieldsMixin, ReviewFormBasic):
    pass
