from django import forms
from unfold.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model

from accounts.models import Profile

UserModel = get_user_model()

class AppUserCreationForm(UserCreationForm):
    class Meta:
        model = UserModel
        fields = ["email"]


class AppUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = UserModel


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']

        labels ={
            'first_name': 'First Name:',
            'last_name': 'Last Name:',
            'birth_date': 'Birth Date:',
            'profile_picture': 'Profile Picture:',
        }
