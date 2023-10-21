from django.urls import path
from . import views

urlpatterns = [
    path('blogs/', views.list_p.as_view(), name='blogs'),
    path('blogs/nueva_publicacion/', views.publicacion_user, name='nueva_publicacion'),
    path('<slug:slug>/', views.detail_p, name="Blog_Post"),
    #re_path(r'^tag/(?P<slug>[-\w]*)/$',views.blog_edit_view.as_view(), name='blog_edit'),
    path('blog_edit/<int:pk>/',views.blog_edit_view.as_view(), name='Blog_Edit'),
    path('blog_delete/<int:pk>/', views.blog_delete_view.as_view(), name='Blog_Delete'),
]
