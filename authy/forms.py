
from django import forms
from django.contrib.auth.forms import UserCreationForm
from ckeditor.widgets import CKEditorWidget
from django.contrib.auth.models import User

class SignInForm(forms.Form):
    
    username=forms.CharField(
        widget=forms.TextInput(
            attrs={
            "placeholder":"username",
            "class":"form-control",
            }))


    password=forms.CharField(
        widget=forms.PasswordInput(
            attrs={
            "placeholder":"password",
            "class":"form-control",
            }))

class SignUpForm(UserCreationForm):
    
    username=forms.CharField(
        widget=forms.TextInput(
            attrs={
            "placeholder":"username",
            "class":"form-control",
                    }))

    email=forms.EmailField(
        widget=forms.EmailInput(
            attrs={
            "placeholder":"email",
            "class":"form-control"
            }))
    
    password1=forms.CharField(
        widget=forms.PasswordInput(
            attrs={
            "placeholder":"password",
            "class":"form-control",
            }))

    password2=forms.CharField(
        widget=forms.PasswordInput(
            attrs={
            "placeholder":"Re-enter password",
            "class":"form-control",
            }))


    class Meta:
        model=User
        fields = ('username', 'email', 'password1', 'password2')

class CommentForm(forms.Form):
      title=forms.CharField(
        widget=forms.TextInput(
            attrs={
            "placeholder":"title",
            "class":"form-control",
                    }))

      email=forms.EmailField(
        widget=forms.EmailInput(
            attrs={
            "placeholder":"email",
            "class":"form-control"
            }))
 

      content=forms.CharField(
        widget=CKEditorWidget(
            attrs={
            "placeholder":"comment",
            "class":"form-control",
            }))
