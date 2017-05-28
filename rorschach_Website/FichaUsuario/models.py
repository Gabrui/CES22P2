from django.db import models

# Create your models here.
#Django transforma cada classe em uma tabela
# e as suas variaveis viram colunas
#isso eh criado no database quando sincronizamos
#o database com o codigo

class UserInfo(models.Model):
    """
        Guarda as informacoes do usuario.
        name: nome do usuario
        email_account: conta de email do usuario
        gender: gênero do usuário.
        country: Pais em que usuario mora.
        home_state_address: estado onde o usuario mora.
        religion: relagiao do usuario
        music_like: gosto musical do usuario
        civil_status: estado civil do usuario
        profession: profissao do usuario
        album_picture: nome do album que guarda as foto do usuario
        age: idedade do usuario
    """
    name = models.CharField(max_length = 250)
    email_account = models.CharField(max_length = 250)
    gender = models.CharField(max_length = 30)
    country = models.CharField(max_length = 250)
    home_state_address = models.CharField(max_length = 250)
    religion = models.CharField(max_length = 250)
    music_like = models.CharField(max_length = 250)
    civil_status = models.CharField(max_length = 100)
    profession = models.CharField(max_length = 100)
    album_picture = models.CharField(max_length = 10000)
    age = models.IntegerField()
    
    def __str__(self):
        
        return self.name + " AND " +self.email_account
    
class Album (models.Model):
    """
        Guarda fotos ou imagens.
    """
    user = models.ForeignKey(UserInfo, on_delete = models.CASCADE)
    user_owner = models.CharField(max_length = 250)
    album_title = models.CharField(max_length = 250)
    genre = models.CharField(max_length = 100)
    album_logo = models.CharField(max_length = 1000)
    
    def __str__(self):
        
        return self.album_title + " owner " + self._user_owner 
    
class Picture(models.Model):
    """
        Representa uma Figura ou Foto.
        album: eh o album ao qual pertence
        file_type: eh a extensao do arquivo imagem
        picture_title: eh o nome da imagem
    """
    album = models.ForeignKey(Album, on_delete = models.CASCADE)
    file_type = models.CharField(max_length = 10)
    picture_title = models.CharField(max_length = 250)
    
    def __str__(self):
        
        return self.picture_title + " from " + self.album
    
    