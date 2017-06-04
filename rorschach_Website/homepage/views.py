from django.views.generic import View
from django.shortcuts import render
from django.views import generic
from FichaUsuario.models import UserInfo, Album
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import redirect

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
        
class PerfilView(generic.DetailView):
    """
        Mostra algumas informacoes do Usuario.
    """
    model = UserInfo
    template_name = "homepage/perfil.html"
    
    def get_context_data(self,**kwargs):
        context = super(PerfilView,self).get_context_data(**kwargs)
        context['pk'] = self.object.pk
        context['username'] = self.object.username
        context['avatar'] = self.object.avatar.url
        context['profession'] = self.object.profession
        context['home_state_address'] = self.object.home_state_address
        context['country'] = self.object.country
        context['age'] = self.object.age
        return context
    
    
class UpdateAccount(UpdateView):
    """
        Mostra um formulario para o usuario atualizar as suas informacoes
    """
    model = UserInfo
    template_name = "homepage/myAccount.html"
    fields = ['name', 'email_account', 'password', 'country', 
                  'home_state_address', 'religion','civil_status', 'profession',
                  'gender', 'age','music_like','avatar']
    
    def get_context_data(self,**kwargs):
        context = super(UpdateAccount,self).get_context_data(**kwargs)
        context['pk'] = self.object.pk
        context['username'] = self.object.username
        context['avatar'] = self.object.avatar.url
        context['profession'] = self.object.profession
        context['home_state_address'] = self.object.home_state_address
        context['country'] = self.object.country
        context['age'] = self.object.age
        context['music_like'] = self.object.music_like
        context['password'] = self.object.password
        context['email_account'] = self.object.email_account
        context['religion'] = self.object.religion
        context['name'] = self.object.name
        context['civil_status'] = self.object.civil_status
        context['gender'] = self.object.gender
         
        return context
    
class AlbumDetailView(generic.DetailView):
    """
     Mostra informacoes do album   
    """
    model = Album
    template_name = "homepage/album.html"
    context_object_name = "all_albums"
    
    def get_context_data(self,**kwargs):
        context = super(AlbumDetailView,self).get_context_data(**kwargs)
        context['pk'] = self.request.user.pk
        context['album_title'] = self.object.username
        context['genre'] = self.object.avatar.url
        context['album_logo'] = self.object.profession
        context['owner'] = self.request.user.username
        context['number_pictures'] = str(len(self.object.picture_set.all()))
        return context
    def get_queryset(self):
        return Album.objects.all()
    
class AlbumAdder(CreateView):
    """
        Cria um novo album para o usuario.
    """     
    model = Album
    template_name = "homepage/addAlbum.html"
    fields=["album_title","genre","album_logo"]
    def form_valid(self,form):
        album = form.save(commit=False)
        album.user = UserInfo.objects.filter(username=self.request.user.username)[0]
        print(album.user)
        album.save()
        return super(AlbumAdder,self).form_valid(form)
    