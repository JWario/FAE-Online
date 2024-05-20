from django.shortcuts import render
#Página de de inicio
def homepage(request):
    return render(request, 'home.html')

#Página de creación de partidas
def CrearPartida(request):
    return render(request, 'crearPartida.html')

#Página para unirse a una partida existente
def Unirse(request):
    return render(request, 'unirse.html')

#Página de herramientas de usuario
def Herramientas(request):
    return render(request, 'herramientas.html')

#Página de comunidad
def Comunidad(request):
    return render(request, 'comunidad.html')

#Creación de usuario
def Login(request):
    return render(request, 'login.html')

#Log de usuario existente
def Logon(request):
    return render(request, 'logon.html')


