from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.views.generic import View
from .forms import UserForm, loginForm
from django.forms import ValidationError
from django.utils.translation import ugettext as _
from .models import UserInfo
# Create your views here.


def index(request):
    
    pass
#-----------------------------fim do metodo index------------------------------

class loginUser(View):
    """
        Representa o metodo de login
    """
    #criando formulario de login
    form_class = loginForm
    #defindo pagina html do login
    template_name = "homepage/homepage.html"
    
    def get(self, request):
        #resposta ao request de get do usuario
        #cria um formulario
        form = self.form_class(None)
        #retorna um formulario login em branco
        return render(request, self.template_name, {'form': form})
    def post(self, request):
        #resposta ao request de post do usuario
        #passa as informacoes do POST para o formulario
        form = self.form_class(request.POST)
        #verificar se tem caracteres estranhos
        form.is_valid()
        #pegar o username e password passados no preenchimento do formulario
        username = form.cleaned_data["login"]
        password = form.cleaned_data["password"]
        #procurar usuario
        user = authenticate(username = username, password = password)
        print(user)
        if user is not None:
                #se existir o usuario e a senha estiver correta
                if user.is_active:
                    #a conta do usuario nao esta banida
                    #logar o usuario
                    login(request, user)
                    #redicionar o usuario para a pagina de perfil
                    return redirect("/homepage/perfil/")
        #se os dados nao forem validos
        #ou usuario nao tiver conta no database
        #ou a conta do usuario estiver banida,
        #ir para a homepage
        return render(request, self.template_name, {'form': form})
#-----------------------Fim da Classe loginUser--------------------------------  
  
class signUp(View):
    """
        representa o cadastro do usuario.
    """
    #cria um objecto do tipo UserForm
    #definido no arquivo forms da pasta FichaUsuario
    form_class = UserForm
    #define o template da pagina do formulario
    template_name = 'homepage/register.html'
    
    def get(self,request):
        #mostra uma pagina formulario em branco
        form = self.form_class(None)
        return render(request, self.template_name, {'form':form})
    
    def post(self, request):
        #trata os dados enviados pelo usuario
        #validando os dados e cadastrando o usuario
        
        #passando as informacoes para o formulario
        form = self.form_class(request.POST)
        #validar as informacoes
        #basicamente verifica caracteres estranhos.
        print("HI")
        if form.is_valid():
            print("valid")
            #cria um objeto form,
            #mas nao salva as informacoes no database
            user = form.save(commit = False)
            
            #normalized user data
            user.username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.age = form.cleaned_data['age']
            user.country = form.cleaned_data['country']
            user.email_account = form.cleaned_data['email_account']
            user.home_state_adress = form.cleaned_data['home_state_adress']
            user.religion = form.cleaned_data['religion']
            user.civil_status = form.cleaned_data['civil_status']
            user.profession = form.cleaned_data['profession']
            user.gender = form.cleaned_data['gender']
            #salva as informacoes do usuario no database
            user.save()
            
            created_user = User.objects.create_user(username = user.username,
                                     email = user.email_account,password=password)
            created_user.save()
            #Aqui acaba o processo de registro do usuario.
            
            #verifica no database se o usuario existe.
            #retorna um objecto User do database
            print(user.username)
            print(password)
            user = authenticate(username = user.username, password = password)
            print(user)
            if user is not None:
                print("authenticated")
                #se o usuario existe
                if user.is_active:
                    print("active")
                    #a conta do usuario nao esta banida
                    #logar o usuario
                    login(request, user)
                    #redicionar o usuario para a pagina de perfil
                    return redirect("/homepage/perfil/")
        #se os dados nao forem validos
        #ou usuario nao tiver conta no database
        #ou a conta do usuario estiver banida,
        #mostrar um formulario em branco
        return render(request, self.template_name, {'form': form})
#--------------------------Fim da Classe singUp-------------------------------- 
    