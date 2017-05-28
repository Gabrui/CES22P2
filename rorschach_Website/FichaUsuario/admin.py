from django.contrib import admin
from .models import UserInfo, Album, Picture
# Register your models here.

admin.site.register(UserInfo)
admin.site.register(Album)
admin.site.register(Picture)