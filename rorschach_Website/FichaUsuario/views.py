from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, User
from django.views.generic import View
from .forms import UserForm, loginForm
from django.forms import ValidationError
from django.utils.translation import ugettext as _
# Create your views here.


def index(request):
    
    pass
#-----------------------------fim do metodo index------------------------------

class loginUser(View):
    
    form_class = loginForm
    
    template_name = "homepage/"
    def get(self, request):
        
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})
    def post(self, request):
        
        form = self.form_class(request.POST)
        #pegando todos os usuarios no database
        listUsers = User.objects.all()
        #verificar o username e o email.
        #gerar processo de erro caso haja um igual
        for user in listUsers: 
            if form.cleaned_data['login'] == user.username() or form.cleaned_data['login'] == user.email_account:
                findUser = user
        
        user = authenticate(username = findUser.username, password = findUser.password) 
        if user is not None:
                #se o usuario existe
                if user.is_active:
                    #a conta do usuario nao esta banida
                    #logar o usuario
                    login(request, user)
                    #redicionar o usuario para a pagina de perfil
                    return redirect("homepage: perfil")
        #se os dados nao forem validos
        #ou usuario nao tiver conta no database
        #ou a conta do usuario estiver banida,
        #mostrar um formulario em branco
        return render(request, self.template_name, {'form': form})
#-----------------------Fim da Classe loginUser--------------------------------  
  
class singup(View):
    """
        representa o cadastro do usuario.
    """
    #cria um objecto do tipo UserForm
    #definido no arquivo forms da pasta FichaUsuario
    form_class = UserForm
    #define o template da pagina do formulario
    template_name = 'homepage/Register.html'
    
    def get(self,request):
        #mostra uma pagina formulario em branco
        form = self.form_class(None)
        return render(request, self.template_name, {'form':form})
    
    def post(self, request):
        #trata os dados enviados pelo usuario
        #validando os dados e cadastrando o usuario
        
        #passando as informacoes para o formulario
        form = self.form_class(request.POST)
        #pegando todos os usuarios no database
        listUsers = User.objects.all()
        #verificar o username e o email.
        #gerar processo de erro caso haja um igual
        for user in listUsers: 
            if form.cleaned_data['username'] == user.username():
                form.add_error("username",ValidationError(_("Username already exist"), code = "invalid"))
            if form.cleaned_data['email_account'] == user.email_account():
                form.add_error("email_account",ValidationError(_("Email Account already exist"), code = "invalid"))
        #validar as informacoes
        #basicamente verifica caracteres estranhos.
        if form.is_valid():
            
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
            user.religion = form.clean_data['religion']
            user.civil_status = form.clean_data['civil_status']
            user.profession = form.clean_data['profession']
            user.gender = form.clean_data['gender']
            #salva as informacoes do usuario no database
            user.save()
            #Aqui acaba o processo de registro do usuario.
            
            #verifica no database se o usuario existe.
            #retorna um objecto User do database
            user = authenticate(username = user.username, password = password)
            
            if user is not None:
                #se o usuario existe
                if user.is_active:
                    #a conta do usuario nao esta banida
                    #logar o usuario
                    login(request, user)
                    #redicionar o usuario para a pagina de perfil
                    return redirect("homepage: perfil")
        #se os dados nao forem validos
        #ou usuario nao tiver conta no database
        #ou a conta do usuario estiver banida,
        #mostrar um formulario em branco
        return render(request, self.template_name, {'form': form})
#--------------------------Fim da Classe singUp-------------------------------- 
    