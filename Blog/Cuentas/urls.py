from . import views
from django.urls import path
from Cuentas.views import ChangePasswordView
from django.contrib.auth.views import LogoutView

app_name = 'Cuentas'

urlpatterns=[
path('login/', views.login_request, name = 'Login'),
path('register/', views.register, name = 'Register'),
path('logout/', LogoutView.as_view(template_name='Cuentas/logout.html'), name='Logout'),
path('profile/', views.profile, name='profile'),
path('password/', ChangePasswordView.as_view(), name="password"),
path('check_profile/',views.profile_info, name="Check_Profile")
]