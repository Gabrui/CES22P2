from django.contrib import admin
from .models import UserInfo, Album, Picture, GenreModel,Score
# Register your models here.

#defindo como o registro de objectos no database
admin.site.register(UserInfo)
admin.site.register(Album)
admin.site.register(Picture)
admin.site.register(GenreModel)
admin.site.register(Score)
#----------------Fim das classes registraveis----------------------------------