from django.urls import path
from .import views
from django.contrib.auth import views as auth_views

urlpatterns=[
    path('',views.home,name='home'),
    path('register/',views.register,name='register'),
    path('login/',views.loggedin,name='login'),
    path('logout/',views.loggedout,name='logout'),
    path('profile/<str:user>/',views.profile,name='profile'),
    path('upload/',views.upload,name='upload'),
    path('fileview/<str:pdf>/',views.fileview,name='fileview'),
    path('fileprofile/<str:pdf>/',views.fileprofile,name='fileprofile'),
    path('filelike/<str:pdf>/',views.filelike,name='filelike'),
    path('filesave/<str:pdf>/',views.filesave,name='filesave'),
    path('save/',views.save,name='save'),
    path('profileedit/',views.profileedit,name='profileedit'),
    path('uploadedit/<str:pdf>/',views.uploadedit,name='uploadedit'),
    path('delupload/<str:pdf>/',views.delupload,name='delupload'),
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='apptest/password_reset.html'), name='password_reset'),
    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(template_name='apptest/password_reset_done.html'), name='password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='apptest/password_reset_confirm.html'), name='password_reset_confirm'),
    path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='apptest/password_reset_complete.html'), name='password_reset_complete'),
]