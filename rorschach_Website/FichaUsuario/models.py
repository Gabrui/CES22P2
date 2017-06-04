from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.core.urlresolvers import reverse
# Create your models here.
# Create your models here.
#Django transforma cada classe em uma tabela
# e as suas variaveis viram colunas
#isso eh criado no database quando sincronizamos
#o database com o codigo

class UserInfo(models.Model):
    """
        Guarda as informacoes do usuario.
        user: Referência ao objeto de autenticação, que guarda login 
        name: nome do usuario
        gender: gênero do usuário.
        country: Pais em que usuario mora.
        home_state_address: estado onde o usuario mora.
        religion: relagiao do usuario
        music_like: gosto musical do usuario
        civil_status: estado civil do usuario
        profession: profissao do usuario
        album_picture: nome do album que guarda as foto do usuario
        age: idedade do usuario
        avatar: arquivo imagem do perfil
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE, default = None)
    name = models.CharField(max_length = 250)
    gender = models.CharField(max_length = 30)
    country = models.CharField(max_length = 250)
    home_state_address = models.CharField(max_length = 250)
    religion = models.CharField(max_length = 250)
    music_like = models.CharField(max_length = 250)
    civil_status = models.CharField(max_length = 100)
    profession = models.CharField(max_length = 100)
    album_picture = models.CharField(max_length = 10000)
    age = models.IntegerField()
    avatar = models.ImageField(max_length = 250, default = "avatar.png")
    

    def __str__(self):        
        return self.name + " AND " +str(self.user)





class Album (models.Model):
    """
        Guarda fotos ou imagens.
    """
    user = models.ForeignKey(UserInfo, on_delete = models.CASCADE)
    album_title = models.CharField(max_length = 250)
    genre = models.CharField(max_length = 100)
    album_logo = models.ImageField(max_length = 1000)
    
    def get_absolute_url(self):
        #definir a url apos a criacao do album
        return reverse("homepage:perfil")
    
    def __str__(self):
        
        return self.album_title + " owner " + self.user.username
    
class Picture(models.Model):
    """
        Representa uma Figura ou Foto.
        album: eh o album ao qual pertence
        picture_file: eh o arquivo imagem
        picture_title: eh o nome da imagem
    """
    album = models.ForeignKey(Album, on_delete = models.CASCADE)
    picture_file = models.ImageField(max_length = 1000, default = None)
    picture_title = models.CharField(max_length = 250)
    
    def get_absolute_url(self):
        #definir a url apos a criacao do album
        return reverse("homepage:perfil",kwargs={'pk': Album.objects.get(pk=self.album.pk).user.pk})
    
    
    def __str__(self):
   
        return self.picture_title + " from " + str(self.album.album_title)

    
    
