from django.shortcuts import render, redirect
# from django.views.generic import TemplateView
from django.views import View
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import ReservaForm
from django.contrib import messages

# Create your views here.

@login_required(login_url='app_reserva:login')
def reservaPage(request):
    form = ReservaForm()
    if request.method == 'POST':
        form = ReservaForm(request.POST)
        if form.is_valid():
            reserva = form.save(commit=False)
            reserva.cliente = request.user
            reserva.save()
            return redirect('home')
        print(form.errors) #Si hay errores, los imprime en la terminal.

    context = {'form':form}

    return render(request, 'reserva.html', context)

def loginPage(request):

    # Si el usuario está logueado, redirecciona al home
    if request.user.is_authenticated: 
        return redirect('app_reserva:reserva')

    # Recibe username y password del formulario
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        #Chequea que el usuario exista
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'El usuario no existe!')

        #Verifica que las credenciales sean correctas
        user = authenticate(request, username=username, password=password)

        #Si existe lo enviamos al home
        if user is not None:
            login(request, user)
            return redirect('app_reserva:reserva')
        else:
            messages.error(request, "Revise sus credenciales")

    context = {}
    return render(request, 'login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('app_reserva:reserva')