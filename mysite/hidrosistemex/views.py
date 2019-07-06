from django.views import View
from django.shortcuts import render, redirect

# Create your views here.

class temperatura (View):
    def get (self,request):
        user = request.user
        context = {
                
            }
        print(user)
        if  user.is_authenticated:
            context['usuario'] = user

        return render (request, 'temperatura.html', context)

class particulas (View):
    def get (self,request):
        user = request.user
        context = {
                
            }
        print(user)
        if  user.is_authenticated:
            context['usuario'] = user

        return render (request, 'particulas.html', context)

class azufre (View):
    def get (self,request):
        user = request.user
        context = {
                
            }
        print(user)
        if  user.is_authenticated:
            context['usuario'] = user

        return render (request, 'azufre.html', context)

class isobutileno (View):
    def get (self,request):
        user = request.user
        context = {
                
            }
        print(user)
        if  user.is_authenticated:
            context['usuario'] = user

        return render (request, 'isobutileno.html', context)

class diocarbono (View):
    def get (self,request):
        user = request.user
        context = {
                
            }
        print(user)
        if  user.is_authenticated:
            context['usuario'] = user

        return render (request, 'diocarbono.html', context)

class monocarbono (View):
    def get (self,request):
        user = request.user
        context = {
                
            }
        print(user)
        if  user.is_authenticated:
            context['usuario'] = user

        return render (request, 'monocarbono.html', context)

class ozono (View):
    def get (self,request):
        user = request.user
        context = {
                
            }
        print(user)
        if  user.is_authenticated:
            context['usuario'] = user

        return render (request, 'ozono.html', context)

class dionitro (View):
    def get (self,request):
        user = request.user
        context = {
                
            }
        print(user)
        if  user.is_authenticated:
            context['usuario'] = user

        return render (request, 'nitrogeno.html', context)

class nitrico (View):
    def get (self,request):
        user = request.user
        context = {
                
            }
        print(user)
        if  user.is_authenticated:
            context['usuario'] = user

        return render (request, 'nitrico.html', context)

class humedad (View):
    def get (self,request):
        user = request.user
        context = {
                
            }
        print(user)
        if  user.is_authenticated:
            context['usuario'] = user

        return render (request, 'humedad.html', context)