from typing import Any
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    photo=models.ImageField(upload_to='profile',default='profile/profile.png')

    def __str__(self):
        return self.user.username
    
class UploadPdf(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    title=models.CharField(max_length=100,null=True,blank=True)
    description=models.TextField(null=True,blank=True)
    pdffile=models.FileField(upload_to='pdf')
    uploaded=models.DateField(auto_now=True)

    def delete(self):
        self.pdffile.delete()
        super().delete()

    def slice(self):
        return f'{self.description[:50]}...'
    
class Views(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    file=models.ForeignKey(UploadPdf,on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username
    
class Likes(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    file=models.ForeignKey(UploadPdf,on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username
    
class Save(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    file=models.ForeignKey(UploadPdf,on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username
    
class Comment(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    file=models.ForeignKey(UploadPdf,on_delete=models.CASCADE)
    comment=models.CharField(max_length=1000,null=True,blank=True)
    posted=models.DateField(auto_now=True)