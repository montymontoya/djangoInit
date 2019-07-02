from django.views import View
from django.shortcuts import render, redirect
from .forms import loginForm, registerForm
from django.contrib.auth import authenticate, login, logout
# Create your views here.
#def index (request):
#    return render (request, 'login.html')

#def register (request):
#    return render (request, 'register.html')

#def login (request):
#    return render (request, 'login.html')

class index (View):
    def get (self,request):
        user = request.user
        context = {
                
            }
        print(user)
        if  user.is_authenticated:
            context['usuario'] = user

        return render (request, 'index.html', context)

def logout_view(request):
    logout(request)
    return redirect('paquito')

class loginIt (View):
    def get(self,request):
        form = loginForm()
        context = {
            'formulario':form
        }
        return render (request, 'login.html', context)
    
    def post(self, request):
        form = loginForm(request.POST)
        context = {
            'formulario':form
        }
        if form.is_valid():
            datos = form.cleaned_data
            print(datos)
            thisUser = datos['usuario']
            thisPass = datos['password']
            user = authenticate(username = thisUser,password = thisPass)
            if user is not None:
                login(request, user)
                print("Exito")

                return redirect('paquito')
            else :
                print("Puro chisme")
                context['error'] = 'nombre de usuario o contraseña invalidos'
                

            return render (request,'login.html', context)
        else :
            print('datos no validos')
            return render (request, 'login.html', context)

class register (View):
    def get(self,request):
        form = registerForm()
        context = {
            'formulario':form
        }
        return render (request, 'register.html', context)
    
    def post(self, request):
        form = registerForm(request.POST)
        context = {
            'formulario':form
        }
        if form.is_valid():
            datos = form.cleaned_data
            print(datos)
            return render (request,'register.html', context)
        else :
            print('datos no validos')
            return render (request, 'register.html', context)



