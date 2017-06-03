from django.views.generic import View
from django.shortcuts import render

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
        