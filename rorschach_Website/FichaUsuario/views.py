from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.views.generic import View
from .forms import UserForm, loginForm
from django.forms import ValidationError
from django.utils.translation import ugettext as _
from .models import UserInfo, Album, Picture,Score, GenreModel
from homepage.views import AuthUser
import random
# Create your views here.



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
        if form.is_valid():
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
    


class SelectRandomImageView(AuthUser,View):
    
    """
        Seleciona aleatoriamente imagens de uma categoria para colocar na tela
        do usuario. Aumenta o score de uma imagem escolhida pelo usuario.
    """
    #Definir nome do template html a ser usado
    template_name = "homepage/grade.html"
    
    def get(self,request,string):
        
        """
            Metodo de resposta ao usuario com request GET.
        """
        #retorna o template html definido anterior
        return render(request,self.template_name, context=self.get_context_data(string))
    
    def get_context_data(self,string): 
        """
            Metodo que fornece variaveis que sao usadas no template html
        """
        pkgenre = GenreModel.objects.get(name=string)
        listAlbum = Album.objects.filter(genre=pkgenre)
        listPicture=[]
        for album in listAlbum: 
            listPicture += album.picture_set.all()
        tamListPicture = len(listPicture)
        if tamListPicture>0:
           dif = False
           while not dif:
               firstImg = random.randint(0,tamListPicture-1)
               secondImg = random.randint(0,tamListPicture-1)
               if firstImg!=secondImg:
                   dif = True
        context = {}
        context["img1"] = listPicture[firstImg].picture_file.url
        context["img2"] = listPicture[secondImg].picture_file.url
        context['pk1'] = listPicture[firstImg].pk
        context['pk2'] = listPicture[secondImg].pk
        #retorna context que possui todas as variaveis usadas no html
        return context
        
    
    def post(self, request,string):
        """
            Metodo de resposta ao request do usuario do tipo POST
        """
        #pegar pk da imagem passada pela url no metodo POST
        img_pk = self.request.POST.get("pk","")
        #pegar object imagem referente ao pk da imagem passado anteriomente
        picture = Picture.objects.get(pk = img_pk)
        #pegar objeto usuario do request
        user = self.request.user
        #pegar objecto UserInfo que contem todas as informacoes do usuario
        userInfo = user.userinfo
        #pegar objecto score referente ao usuario e da imagem
        score = Score.objects.filter(user=userInfo, picture=picture)
        if score:
            #se existir aumenta o score
            #aumentar score
            score[0].total_score +=1
            #salvar alteracao
            score[0].save()
            
        else:
            #se nao existir, cria um score atrelado ao usuario e ah imagem
            picture.score_set.create(total_score = 1,user=userInfo)
        #redireciona para propria pagina para fornacer novas imagens
        #para serem escolhidas
        return redirect(".")
#--------------------Fim da Classe SelectRandomimageView-----------------------





class RankView(View):
    """
        Fornece uma lista ordenada de acordo com os scores de imagens de uma
        categoria escolhida pelo usuario e de fitros escolhidos pelo usuario.
    """
    
    #definir template html a ser usado
    template_name = "homepage/ranking.html"
    
    def get(self,request,category,criteria):
        """
            metodo que responde ao request GET. Retornando um template com as 
            imagens ordanadas por score.
        """
       
        #retorna o template html
        return render(request,self.template_name, context=self.get_context_data(category))        
    
    def get_context_data(self,category):
        """
            Metodo que fornece as variaveis que sao usadas no codigo html.
        """
        SortedList=[]
        if category:
            
            pk_genre = GenreModel.objects.get(name=category)
            albumList = Album.objects.filter(genre = pk_genre)
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
                SortedList = sorted(listfinal, key=lambda x: x[0], reverse=True)
        context = {}
        context["SortedList"] = SortedList
        #retorna context que contem todas as variaveis usadas no html
        return context
#-------------------------Fim da Classe RankView-------------------------------  



