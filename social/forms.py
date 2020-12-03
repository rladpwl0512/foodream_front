from django.contrib.auth.models import User
from django import forms
from .models import TestUserProfile

class SignupForm(forms.Form):
    class Meta:
        model = User
    address = forms.CharField(max_length=64, widget=forms.TextInput(attrs={'placeholder':'주소'}))
    phone_number = forms.CharField(max_length=32, widget=forms.TextInput(attrs={'placeholder':'010-0000-0000'}))
    registration_number = forms.CharField(max_length=32, widget=forms.TextInput(attrs={'placeholder':'000000-0000000'}))

    def signup(self, request, user):
        userProfile = TestUserProfile()
        userProfile.user = user
        userProfile.address = self.cleaned_data['address']
        userProfile.phone_number = self.cleaned_data['phone_number']
        userProfile.registration_number = self.cleaned_data['registration_number']
        userProfile.save()
        user.save()
        return user