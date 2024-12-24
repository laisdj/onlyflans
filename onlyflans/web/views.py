from django.shortcuts import render, redirect
from .models import Flan, ContactForm
from django.http import HttpResponse,HttpResponseRedirect
from .forms import ContactFormForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import RegistroForm

# Create your views here.
def indice(request):
    # Filtrar los flanes que no son privados (públicos)
    flanes_publicos = Flan.objects.filter(is_private=False)
    
    # Pasar los flanes públicos al contexto
    return render(request, 'index.html', {'flanes_publicos': flanes_publicos})

def acerca(request):
    return render(request, 'about.html')

@login_required
def bienvenidos(request):
    # Filtrar los flanes privados
    flanes_privados = Flan.objects.filter(is_private=True)
    
    # Obtener el nombre de usuario
    full_name = request.user.get_full_name()  # O usa request.user.get_full_name() para el nombre completo
    
    # Pasar los flanes privados y el nombre de usuario al contexto
    return render(request, 'welcome.html', {'flanes_privados': flanes_privados, 'full_name': full_name})

def contacto(request):
    if request.method == 'POST':
        form = ContactFormForm(request.POST)

        if form.is_valid():

            contact_form = ContactForm.objects.create(**form.cleaned_data)
            

            return redirect('contacto_exito')
        

    else:
        form = ContactFormForm()
    
    return render(request, 'contacto.html', {'form':form})

def exito(request):
    return render(request, 'exito.html', {'message': 'Gracias por contactarte con OnlyFlans, te responderemos en breve.'})



def usuario_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('bienvenidos')  # Redirige a la página de bienvenida
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})

@login_required
def usuario_logout(request):
    # Limpiar mensajes previos
    messages.get_messages(request).used = True
    logout(request)
    messages.success(request, "Has cerrado sesión exitosamente.")
    return redirect('indice')



def registro_view(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.first_name = form.cleaned_data['name']
            user.save()
            login(request, user)
            messages.success(request, "Usuario creado exitosamente.")
            return redirect('bienvenidos')
    else:
        form = RegistroForm()
    
    return render(request, 'registro.html', {'form': form})