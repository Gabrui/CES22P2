from django.views.generic import View
from django.shortcuts import render

# Create your views here.
#This File receive client request and send back the response

class IndexView(View):
    
    #nome do template da pagina em html
    template_name = "homepage/homepage.html"
    
    def get(self,request):
        #metodo de resposta ao request get do cliente
        #retorna a pagina html
        return render(request, self.template_name)

class PerfilView(View):
    
    #nome do template da pagina em html
    template_name = "homepage/perfil.html"
    
    def get(self,request):
        #metodo de resposta ao request get do cliente
        #retorna a pagina html
        return render(request, self.template_name)
