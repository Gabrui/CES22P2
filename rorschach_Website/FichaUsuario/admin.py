from django.contrib import admin
from .models import UserInfo, Album, Picture
# Register your models here.

#defindo como o registro de objectos no database
admin.site.register(UserInfo)
admin.site.register(Album)
admin.site.register(Picture)
#----------------Fim das classes registraveis----------------------------------