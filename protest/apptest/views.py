from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from .models import *
from .forms import *
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.

def register(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        if request.method=='POST':
            firstname=request.POST.get('firstname')
            lastname=request.POST.get('lastname')
            username=request.POST.get('username')
            email=request.POST.get('email')
            password1=request.POST.get('password1')
            password2=request.POST.get('password2')
            photo=request.FILES.get('photo')
            if firstname and lastname and username and email and password1 and password2:
                if password1==password2:
                    if User.objects.filter(Q(username=username)|Q(email=email)).exists():
                        messages.error(request,'User or Email Already Exists !')
                    else:
                        user=User.objects.create_user(first_name=firstname,last_name=lastname,username=username,email=email,password=password1)
                        if photo is not None:
                            profile=Profile.objects.create(user=user,photo=photo)
                        else:
                            profile=Profile.objects.create(user=user,photo='profile/profile.png')
                        user.save()
                        profile.save()
                        return redirect('login')
                else:
                    messages.error(request,'Incorrect Password !')
            else:
                return redirect('register')
    return render(request,'apptest/register.html')

def loggedin(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        if request.method=='POST':
            username=request.POST.get('username')
            password=request.POST.get('password')

            if username and password:
                user=authenticate(username=username,password=password)

                if user is not None:
                    login(request,user)
                    return redirect('/')
                else:
                    messages.error(request,'Incorrect Username or Password !')
            else:
                return redirect('login')
    return render(request,'apptest/login.html')

def loggedout(request):
    logout(request)
    return redirect('login')

def home(request):
    if request.method=='POST':
        q=request.POST.get('q')
        pdfs=UploadPdf.objects.filter(Q(title__icontains=q)|Q(description__icontains=q)|Q(user__username__icontains=q)).order_by('-id')
    else:
        pdfs=UploadPdf.objects.all().order_by('-id')
    context={'pdfs':pdfs}
    return render(request,'apptest/home.html',context)

@login_required(login_url='login')
def profile(request,user):
    user=User.objects.get(id=user)
    photo=Profile.objects.get(user=user)
    pdfs=UploadPdf.objects.filter(user=user).order_by('-id')
    nopdfs=UploadPdf.objects.filter(user=user).count()
    context={'user':user,'photo':photo,'pdfs':pdfs,'nopdfs':nopdfs}
    return render(request,'apptest/profile.html',context)

@login_required(login_url='login')
def upload(request):
    form=UploadPdfForm()
    if request.method=='POST':
        form=UploadPdfForm(request.POST,request.FILES)
        if form.is_valid():
            instance=form.save(commit=False)
            instance.user=request.user
            instance.save()
            return redirect('/')
        else:
            return redirect('upload')
    context={'form':form}
    return render(request,'apptest/upload.html',context)

@login_required(login_url='login')
def filelike(request,pdf):
    pdf=UploadPdf.objects.get(id=pdf)
    if Likes.objects.filter(user=request.user,file=pdf).exists():
        like=Likes.objects.get(user=request.user,file=pdf)
        like.delete()
        return redirect('fileview',pdf.id)
    else:
        like=Likes.objects.create(user=request.user,file=pdf)
        like.save()
        return redirect('fileview',pdf.id)

@login_required(login_url='login')
def fileview(request,pdf):
    likeshow=False
    saveshow=False
    pdf=UploadPdf.objects.get(id=pdf)
    form=CommentForm()
    if request.method=='POST':
        form=CommentForm(request.POST)
        if form.is_valid():
            instance=form.save(commit=False)
            instance.user=request.user
            instance.file=pdf
            instance.save()
            return redirect('fileview',pdf.id)
    comments=Comment.objects.filter(file=pdf).order_by('-id')
    if Likes.objects.filter(user=request.user,file=pdf).exists():
        likeshow=True
    else:
        likeshow=False
    if Save.objects.filter(user=request.user,file=pdf).exists():
        saveshow=True
    else:
        saveshow=False
    if Views.objects.filter(user=request.user,file=pdf).exists():
        pass
    else:
        view=Views.objects.create(user=request.user,file=pdf)
        view.save()
    context={'pdf':pdf,'likeshow':likeshow,'saveshow':saveshow,'form':form,'comments':comments}
    return render(request,'apptest/fileview.html',context)

@login_required(login_url='login')
def fileprofile(request,pdf):
    pdfview=UploadPdf.objects.get(id=pdf)
    photo=Profile.objects.get(user=pdfview.user.id)
    views=Views.objects.filter(file=pdf).count()
    likes=Likes.objects.filter(file=pdf).count()
    comments=Comment.objects.filter(file=pdf).count()
    context={'pdfview':pdfview,'views':views,'photo':photo,'likes':likes,'comments':comments}
    return render(request,'apptest/fileprofile.html',context)

@login_required(login_url='login')
def filesave(request,pdf):
    pdf=UploadPdf.objects.get(id=pdf)
    if Save.objects.filter(user=request.user,file=pdf).exists():
        save=Save.objects.filter(user=request.user,file=pdf)
        save.delete()
        return redirect('fileview',pdf.id)
    else:
        save=Save.objects.create(user=request.user,file=pdf)
        save.save()
        return redirect('fileview',pdf.id)

@login_required(login_url='login')
def save(request):
    saves=Save.objects.filter(user=request.user)
    context={'saves':saves}
    return render(request,'apptest/save.html',context)

@login_required(login_url='login')
def profileedit(request):
    photo=Profile.objects.get(user=request.user)
    profileform=ProfileUpdateForm(instance=request.user)
    photoform=ProfilePhotoUpdateForm(instance=photo)
    if request.method=='POST':
        profileform=ProfileUpdateForm(request.POST,instance=request.user)
        photoform=ProfilePhotoUpdateForm(request.POST,request.FILES,instance=photo)
        if profileform.is_valid() and photoform.is_valid():
            instance=photoform.save(commit=False)
            instance.user=request.user
            instance.save()
            profileform.save()
            return redirect('profile',request.user.id)
    context={'photoform':photoform,'profileform':profileform}
    return render(request,'apptest/profileedit.html',context)

@login_required(login_url='login')
def uploadedit(request,pdf):
    pdf=UploadPdf.objects.get(id=pdf)
    form=UploadPdfUpdateForm(instance=pdf)
    if request.method=='POST':
        form=UploadPdfUpdateForm(request.POST,instance=pdf)
        if form.is_valid():
            form.save()
            return redirect('fileprofile',pdf.id)
    context={'form':form,'pdf':pdf}
    return render(request,'apptest/uploadedit.html',context)

@login_required(login_url='login')
def delupload(request,pdf):
    pdf=UploadPdf.objects.get(id=pdf)
    if request.method=='POST':
        pdf.delete()
        return redirect('/')
    context={'pdf':pdf}
    return render(request,'apptest/delupload.html',context)