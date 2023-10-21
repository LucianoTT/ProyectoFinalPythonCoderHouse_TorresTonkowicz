from django.views import generic
from .models import publicacion_model
from .forms import comentarios_form, nueva_publi_form
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views.generic.edit import UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

#Funcion que ordena y muestra todas las publicaciones en pantalla
class list_p(generic.ListView):
    queryset = publicacion_model.objects.all().order_by('-publication_date')
    template_name = "Mensajeria/Publicaciones.html"

#Funcion para las publicaciones y comentarios
def detail_p(request, slug):
    template_name = 'Mensajeria/blog_post.html'
    post = get_object_or_404(publicacion_model, slug=slug)
    comments = post.Comentarios.filter
    nuevo_comentario = None
    if request.method == 'POST':
        comentarioform = comentarios_form(data=request.POST)
        if comentarioform.is_valid():
            nuevo_comentario = comentarioform.save(commit=False)
            nuevo_comentario.post = post
            nuevo_comentario.name = request.user
            nuevo_comentario.save()
    else:
        comentarioform= comentarios_form()
    return render(request, template_name, {'post': post, 'comments': comments, 'nuevo_comentario': nuevo_comentario, 'comentarioform': comentarioform})

#Funcion para que el usuario cree nuevas publicaciones blog.
@login_required
def publicacion_user(request):
    template_name= 'Mensajeria/Nueva_publi.html'
    if request.method == 'POST':
        nueva_publicacion= nueva_publi_form(request.POST, request.FILES)
        if  nueva_publicacion.is_valid():
            task_list = nueva_publicacion.save(commit=False)
            task_list.author = request.user
            task_list.save()
            return redirect('/')
    else:
        nueva_publicacion = nueva_publi_form()
    return render(request, template_name, {'nueva_publicacion':nueva_publicacion})

#Funcion basada en clases para editar un blog ya publicado.
class blog_edit_view(LoginRequiredMixin, UpdateView):
    model = publicacion_model
    success_url = reverse_lazy("blogs")
    fields = ["id","title","subtitle","body","imagen"]
    template_name = 'Mensajeria/editar_blog.html'

#Funcion basada en clases para eliminar un blog publicado.
class blog_delete_view(LoginRequiredMixin, DeleteView):
    model = publicacion_model
    success_url = reverse_lazy("blogs")
    template_name = 'Mensajeria/eliminar_blog.html'