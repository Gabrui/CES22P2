from django.views.generic import View
from django.shortcuts import render
from django.views import generic
from FichaUsuario.models import UserInfo
from django.views.generic.edit import CreateView, UpdateView, DeleteView

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
    model = UserInfo
    template_name = "homepage/myAccount.html"
    fields = ['name','username', 'email_account', 'password', 'country', 
                  'home_state_address', 'religion','civil_status', 'profession',
                  'gender', 'age','music_like','avatar']
    