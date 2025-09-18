from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse
from .forms import CustomUserCreationForm, CustomLoginForm

def home_view(request):
    """Vista para la página principal"""
    return render(request, 'accounts/home.html')

def register_view(request):
    """Vista para el registro de usuarios"""
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'¡Cuenta creada exitosamente para {username}! Ya puedes iniciar sesión.')
            return redirect('login')
        else:
            messages.error(request, 'Por favor corrige los errores del formulario.')
    else:
        form = CustomUserCreationForm()
    
    return render(request, 'accounts/register.html', {'form': form})

def login_view(request):
    """Vista para el login de usuarios"""
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == 'POST':
        form = CustomLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                login(request, user)
                messages.success(request, f'¡Bienvenido de vuelta, {user.first_name}!')
                next_page = request.GET.get('next')
                return redirect(next_page) if next_page else redirect('dashboard')
            else:
                messages.error(request, 'Usuario o contraseña incorrectos.')
        else:
            messages.error(request, 'Por favor corrige los errores del formulario.')
    else:
        form = CustomLoginForm()
    
    return render(request, 'accounts/login.html', {'form': form})

@login_required
def dashboard_view(request):
    """Vista del dashboard para usuarios autenticados"""
    return render(request, 'accounts/dashboard.html')

@login_required
def logout_view(request):
    """Vista para el logout de usuarios"""
    logout(request)
    messages.success(request, '¡Sesión cerrada exitosamente!')
    return redirect('home')

@login_required
def profile_view(request):
    """Vista para mostrar el perfil del usuario"""
    profile = request.user.userprofile
    context = {
        'profile': profile,
        'user': request.user
    }
    return render(request, 'accounts/profile.html', context)
