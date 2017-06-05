from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.views.generic import View
from .forms import UserForm, loginForm
from django.forms import ValidationError
from django.utils.translation import ugettext as _
from .models import UserInfo, Album, Picture,Score
import random
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
        """
        Resposta ao request de get do usuario: Invalida
        """
        # Cria um formulario
        form = self.form_class(None)
        # Retorna um formulario login em branco
        return render(request, self.template_name, {'form': form})
    
    
    def post(self, request):
        """
        Resposta ao request de post do usuario: A ser validade
        """
        # Passa as informacoes do POST para o formulario
        form = self.form_class(request.POST)
        # Verificar se tem caracteres estranhos
        if form.is_valid():
            # Pega o username e password passados no preenchimento do formulario
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            # Procura usuario
            user = authenticate(username = username, password = password)
            # Se existir o usuario e a senha estiver correta
            if user is not None:
                # Se a conta do usuario nao esta banida
                if user.is_active:
                    # Logar o usuario
                    login(request, user)
                    return redirect("homepage:perfil")
        #se os dados nao forem validos
        #ou usuario nao tiver conta no database
        #ou a conta do usuario estiver banida,
        #ir para a homepage
        return render(request, self.template_name, {'form': form})
#-----------------------Fim da Classe loginUser--------------------------------  




  
class signUp(View):
    """
    Representa o cadastro do usuario.
    """
    # Cria um objecto do tipo UserForm
    # Definido no arquivo forms da pasta FichaUsuario
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
        print('post')
        if form.is_valid():
            print('valido')
            # Cria um objeto form,mas nao salva as informacoes no database
            userInfo = form.save(commit = False)
            
            # Infomações extraídas do formulário
            username = form.cleaned_data['username']
            email_account = form.cleaned_data['email_account']
            password = form.cleaned_data['password']
            
            #criar objeto usuario
            #e passar as informacoes basicas
            created_user = User.objects.create_user(username = username,
                                     email = email_account, password=password)
            userInfo.user = created_user
            #salvar usuario
            created_user.save()
            userInfo.save()
            #Aqui acaba o processo de registro do usuario.
            
            # Procura usuario
            user = authenticate(username = username, password = password)
            # Se existir o usuario e a senha estiver correta
            if user is not None:
                # Se a conta do usuario nao esta banida
                if user.is_active:
                    # Logar o usuario
                    login(request, user)
                    return redirect("homepage:perfil")
        #se os dados nao forem validos
        #ou usuario nao tiver conta no database
        #ou a conta do usuario estiver banida,
        #mostrar um formulario em branco
        return render(request, self.template_name, {'form': form})
#--------------------------Fim da Classe singUp-------------------------------- 
    

#random.randint(a,b)

class SelectRandomImageView(View):
    
    """
        Seleciona aleatoriamente imagens de uma categoria para colocar na tela
        do usuario. Aumenta o score de uma imagem escolhida pelo usuario.
    """
    template_name = "homepage/grade.html"
    
    def get(self,request,string):
        
       return render(request,self.template_name, context=self.get_context_data(string))
    
    def get_context_data(self,string): 
       listAlbum = Album.objects.filter(genre=string)
       listPicture=[]
       for album in listAlbum: 
            listPicture += album.picture_set.all()
       tamListPicture = len(listPicture)
       if tamListPicture>0:
           dif = False
           while not dif:
               firstImg = random.randint(0,tamListPicture)
               secondImg = random.randint(0,tamListPicture)
               if firstImg!=secondImg:
                   dif = True
       context = {}
       context["img1"] = listPicture[firstImg].picture_file.url
       context["img2"] = listPicture[secondImg].picture_file.url
       context['pk1'] = listPicture[firstImg].pk
       context['pk2'] = listPicture[secondImg].pk
        
       return context
        
    def post(self, request,string):
        
        img_pk = self.request.POST.get("pk","")
        picture = Picture.objects.get(pk = img_pk)
        user = self.request.user
        userInfo = user.userinfo
        score = Score.objects.get(user=userInfo)
        if score:
            
            score.total_score+=1
            
        else:
            
            picture.score_set.create(total_score=1,user=userInfo)
            
        return redirect(".")
#--------------------Fim da Classe SelectRandomimageView-----------------------

class RankView(View):
    """
        Fornece uma lista ordenada de acordo com os scores de imagens de uma
        categoria escolhida pelo usuario e de fitros escolhidos pelo usuario.
    """
    
    template_name = "homepage/rankview.html"
    
    def get(self,request,category,criteria):
        """
            metodo que responde ao request GET. Retornando um template com as 
            imagens ordanadas por score.
        """
       
        return render(request,self.template_name, context=self.get_context_data(category))        
    
    def get_context_data(self,category):
        
        SortedList=[]
        if category:
            
            albumList = Album.objects.filter(genre = category)
            pictureList = []
            listfinal = []
            
            if albumList:
                for album in albumList:
                
                    pictureList = album.picture_set.all()
                    for picture in pictureList:
                        
                        scoreList = picture.score_set.all()
                        newscore = 0
                        for score in scoreList:
                            newscore += score.total_score
                        listfinal.append((newscore, picture))
                SortedList = sorted(listfinal, key=lambda x: x[0])
        context = {}
        context["SortedList"] = SortedList
        return context
    



