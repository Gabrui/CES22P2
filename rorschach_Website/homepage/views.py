from django.views.generic import View
from django.shortcuts import render
from django.views import generic
from FichaUsuario.models import UserInfo
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
    model = UserInfo
    template_name = "homepage/perfil.html"
    
    def get_object(self):
        return self.request.user.userinfo
    
    
    
    
    
class UpdateAccount(AuthUser, UpdateView):
    model = UserInfo
    template_name = "homepage/myAccount.html"
    fields = ['name', 'country', 'home_state_address', 'religion',
              'civil_status', 'profession','gender', 'age','music_like','avatar']
    
    def get_object(self):
        return self.request.user.userinfo
    
        
        
        
        