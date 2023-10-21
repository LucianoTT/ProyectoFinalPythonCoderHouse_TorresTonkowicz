from Main import views
from django.urls import path

app_name = 'Main'

urlpatterns = [
    path('', views.index, name="index"),
    path('about/', views.about, name="about"),
]
