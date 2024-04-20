from django.contrib import admin
from .models import *

# Register your models here.

class UploadPdfAdmin(admin.ModelAdmin):
    list_display=['user','title','uploaded']

class CommentAdmin(admin.ModelAdmin):
    list_display=['user','file','posted']

admin.site.register(Profile)
admin.site.register(UploadPdf,UploadPdfAdmin)
admin.site.register(Views)
admin.site.register(Likes)
admin.site.register(Comment,CommentAdmin)
