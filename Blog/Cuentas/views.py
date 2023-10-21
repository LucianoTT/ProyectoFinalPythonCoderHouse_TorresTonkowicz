from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from .forms import UserRegisterForm, edit_profile, edit_user
from django.contrib import messages
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordChangeView
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import UpdateView


#Función para el login de los usuarios ya registrados.
def login_request(request):
    if request.user.is_authenticated:
        return redirect("/")
    if request.method == "POST":
        form = AuthenticationForm(request, data = request.POST)
        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            contra = form.cleaned_data.get('password')
            user = authenticate(username=usuario, password=contra)
            if user is not None:
                login(request, user)
                return render(request, "Main/index.html")
            else:
                messages.error(request, 'Username or password is wrong')
                return redirect('login/')
    else:        
        form = AuthenticationForm()
    return render(request,"Cuentas/login.html", {'form':form})

#Función para el registro de nuevos usuarios.
def register(request):
    if request.user.is_authenticated:
        return redirect("/")
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            form.save()
            return redirect('/login/')
    else:
        form = UserRegisterForm()
    return render(request, "Cuentas/register.html", {"form":form})

#Función para editar todos los datos de las cuentas registradas.
@login_required
def profile(request):
    if request.method == 'POST':
        user_form = edit_user(request.POST, instance=request.user)
        profile_form = edit_profile(request.POST,request.FILES, instance=request.user.avatar)
        if user_form.is_valid() and profile_form.is_valid():
            profile_form.save()
            user_form.save()

            messages.success(request, 'Cambiado con exito!')
            return redirect(to='/check_profile/')
    else:
        user_form= edit_user(instance=request.user)
        profile_form=edit_profile(instance=request.user.avatar)
    return render(request,'Cuentas/profile.html', {'user_form': user_form, 'profile_form': profile_form})

#Función para cambiar la contraseña.
class ChangePasswordView(SuccessMessageMixin, PasswordChangeView):
    template_name = 'Cuentas/password.html'
    success_message = "Successfully Changed Your Password"
    success_url = reverse_lazy("Main:index")

#Función para mostrar la información de la cuenta logeada.
@login_required
def profile_info(request):
    return render(request, 'Cuentas/check_profile.html')


