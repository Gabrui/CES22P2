from django.views.generic import View
from django.shortcuts import render
from django.views import generic
from FichaUsuario.models import UserInfo, Album, Picture, GenreModel
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
#This File receive client request and send back the response



class SendTemplateView(View):
    """
        Classe abstrata que envia um template html
        Usada quando uma url tem como resposta apenas o envio de um template
        template_name: nome do arquivo template html
    """
    template_name = "homepage/homepage.html"
    
    def get(self,request):
        #metodo de resposta ao request get do cliente
        #retorna a pagina html
        return render(request, self.template_name)
        



class AuthUser(LoginRequiredMixin):
    login_url = "/loginUser"
    redirect_field_name = ""



    
    
class PerfilView(AuthUser, generic.DetailView):
    """
        Mostra algumas informacoes do Usuario.
    """
    model = UserInfo
    template_name = "homepage/perfil.html"
    
    def get_object(self):
        self.all_albums = self.request.user.userinfo.album_set.all()
        return self.request.user.userinfo
    
    


class UpdateAccount(AuthUser, UpdateView):
    """
        Mostra um formulario para o usuario atualizar as suas informacoes
    """
    model = UserInfo
    template_name = "homepage/myAccount.html"
    fields = ['name', 'country', 
                  'home_state_address', 'religion','civil_status', 'profession',
                  'gender', 'age','music_like','avatar']
    
    def get_object(self):
        return self.request.user.userinfo
    
    
    
    
class AlbumDetailView(AuthUser, generic.DetailView):
    """
     Mostra informacoes do album   
    """
    model = Album
    template_name = "homepage/album.html"
    
    def get_context_data(self,**kwargs):
        context = generic.DetailView(self).get_context_data(**kwargs)
        context['pk'] = self.request.user.pk
        context['album_title'] = self.object.album_title
        context['genre'] = self.object.genre
        context['album_logo'] = self.object.album_logo.url
        context['owner'] = self.request.user.username
        context['number_pictures'] = str(len(self.object.picture_set.all()))
        context['albumpk'] = self.object.pk
        context["all_picture"] = self.object.picture_set.all()
        return context




class AlbumAdder(AuthUser, CreateView):
    """
        Cria um novo album para o usuario.
    """     
    model = Album
    template_name = "homepage/addAlbum.html"
    fields=["album_title","genre","album_logo"]
    
    
    def form_valid(self,form):
        album = form.save(commit=False)
        album.user = self.request.user.userinfo
        print(album.user)
        album.save()
        return super(AlbumAdder,self).form_valid(form)




class PictureDetailView(AuthUser, generic.DetailView):
    """
     Mostra informacoes do album   
    """
    model = Picture
    template_name = "homepage/picture.html"
    
    def get_context_data(self,**kwargs):
        context = super(PictureDetailView,self).get_context_data(**kwargs)
        context['pk'] = self.request.user.pk
        context['picture_title'] = self.object.picture_title
        context['genre'] = Album.objects.get(pk=self.object.album.pk).genre
        context['picture_logo'] = self.object.picture_file.url

        return context
    



class PictureAdder(AuthUser, CreateView):
    """
        Cria um novo album para o usuario.
    """     
    model = Picture
    template_name = "homepage/addPicture.html"
    fields=["picture_title","picture_file"]
    def form_valid(self,form):
        form.instance.album_id = self.kwargs.get('pk')
        print(form.instance.album_id)
        
        return super(PictureAdder,self).form_valid(form)
     
