from django import forms
from .models import *
from django.contrib.auth.models import User

class UploadPdfForm(forms.ModelForm):
    class Meta:
        model=UploadPdf
        fields=['title','description','pdffile']

class CommentForm(forms.ModelForm):
    class Meta:
        model=Comment
        fields=['comment']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','first_name','last_name','email']

class ProfilePhotoUpdateForm(forms.ModelForm):
    class Meta:
        model=Profile
        fields=['photo']

class UploadPdfUpdateForm(forms.ModelForm):
    class Meta:
        model=UploadPdf
        fields=['title','description']