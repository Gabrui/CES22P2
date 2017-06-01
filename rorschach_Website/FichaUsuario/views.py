from django.shortcuts import render
from django.shorcuts import redirect
from django.contrib.auth import authenticate, login
from django.views.generic import View
from .forms import UserForm


# Create your views here.


def index(request):
    
    pass

class singup(View):
    
    form_class = UserForm
    template_name = 'homepage/Register.html'
    
    def get(self,request):
        
        form = self.form_class(None)
        return render(request, self.template_name, {'form':form})
    
    def post(self, request):
        
        form = self.form_class(request.POST)
        
        if form.is_valid():
            
            #create a object from the form, but dont save to database
            user = form.save(commit = False)
            
            #cleaned (normalized) data
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()
            
            user = authenticate(username = username, password = password)
            
            if user is not None:
                
                if user.is_active:
                    
                    login(request, user)
                    return redirect("homepage: perfil")
        return render(request, self.template_name, {'form': form})
    
    