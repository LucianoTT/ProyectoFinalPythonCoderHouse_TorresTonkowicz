from django.contrib import admin
from .models import publicacion_model, comentarios

class publicacion_admin(admin.ModelAdmin):
    list_display= ('title','slug','publication_date','author')
    search_fields= ['title', 'body']
    prepopulated_fields = {'slug':('title',)}

admin.site.register(publicacion_model, publicacion_admin)

@admin.register(comentarios)
class comentario_admin(admin.ModelAdmin):
    list_display= ('post','body','publication_date')
    list_filter= ["publication_date"]
    search_field= ['body']

