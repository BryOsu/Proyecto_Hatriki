from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib import messages
from django.views import View
from django.http import HttpResponse
from .models import RegisterUser
from .forms import RegisterUserForm, EditProfileForm


# Vista para el registro de user
class RegisterView(View):
    def get(self, request):
        form = RegisterUserForm()
        return render(request, 'register_user.html', {'form': form})

    def post(self, request):
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            user = form.save(form)
            login(request, user)
            return redirect('login')
        return render(request, 'register_user.html', {'form': form})

# Vista para el login de user
class LoginView(View):
    def get(self, request):
        form = AuthenticationForm()
        return render(request, 'login.html', {'form': form})

    def post(self, request):
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('start')
                else:
                    messages.error(request, "Tu cuenta está inactiva.")
            else:
                messages.error(request, "Nombre de usuario o contraseña incorrectos.")
        else:
            messages.error(request, "Nombre de usuario o contraseña incorrectos.")
            
        return render(request, 'login.html', {'form': form})

# Vista para el logout de user
class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('login')
    

class ProfileView(View):
    @method_decorator(login_required)
    def get(self, request):
        form = EditProfileForm(instance=request.user)
        return render(request, 'profile.html', {'form': form})

    @method_decorator(login_required)
    def post(self, request):
        form = EditProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            print("Form data:", form.cleaned_data)  # Esto imprimirá los datos que se están procesando
            form.save()
            messages.success(request, 'Profile updated successfully.')
            return redirect('start')
        else:
            print("Form errors:", form.errors)  # Esto imprimirá los errores en caso de que el formulario no sea válido
        return render(request, 'profile.html', {'form': form})