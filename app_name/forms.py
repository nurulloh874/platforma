from django import forms
from django.contrib.auth.models import User
from .models import Profile
from django.contrib.auth.forms import UserCreationForm
from .models import User, Project

# Ro'yxatdan o'tish formasi
class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    birth_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
            Profile.objects.create(
                user=user,
                birth_date=self.cleaned_data['birth_date']
            )
        return user
    

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'birth_date', 'password1', 'password2']

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'description', 'image']
