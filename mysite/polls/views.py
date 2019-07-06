from django.views import View
from django.shortcuts import render, redirect
from .forms import loginForm, registerForm, registrarImpresion
from django.contrib.auth import authenticate, login, logout, get_user
from django.contrib.auth.models import User
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
            user = User.objects.create_user(datos['usuario'], datos['correo'], datos['password'])
            user.first_name = datos['nombre']
            user.save()
            print(user)
            
            return redirect('logueadito')
        else :
            print('datos no validos')
            return render (request, 'register.html', context)

class tabladeUsuarios(View):
    def get(self, request):
        users = User.objects.all()
        context = {
           'datosUser':users
        }
        print(users)
        return render (request, 'tablaUsuarios.html',context)


class editarUsuario(View):
    def get(self, request, id):
        user = User.objects.get(pk=id)
        context = {
            'datosUser':user
        }
        print(user)
        return render (request, 'editarUsuario.html',context)

class registerImpresion (View):
    def get(self,request):
        form = registrarImpresion()
        context = {
            'formulario':form
        }
        return render (request, 'regImpresion3D.html', context)
    
    def post(self, request):
        form = registrarImpresion(request.POST)
        context = {
            'formulario':form
        }
        if form.is_valid():
            datos = form.cleaned_data
            printType = User.objects.create_user(datos['nombre'],datos['gramaje'], datos['tiempo'], datos['cantidad'])
            printType.save()
            print(printType)
            
            return redirect('impresito')
        else :
            print('datos no validos')
            return render (request, 'regImpresion3D.html', context)
