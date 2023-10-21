from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from Mensajeria.slug import unique_slugify

class publicacion_model(models.Model):
    title=models.CharField(max_length=100, unique=True)
    subtitle=models.CharField(max_length=100)
    slug=models.SlugField(max_length=100, unique=True)
    author=models.ForeignKey(User, on_delete= models.CASCADE, related_name='blog_publicacion')
    body=models.TextField()
    publication_date = models.DateTimeField(default=timezone.now)
    imagen = models.ImageField(upload_to='images', null=True, blank = True)

    def save(self, **kwargs):
        slug = '%s' % (self.title)
        unique_slugify(self, slug)
        super(publicacion_model, self).save()

    class Meta:
        ordering = ['-publication_date']

    def __str__(self):
        return self.title
    
class comentarios(models.Model):
    name = models.CharField(max_length=80)
    post = models.ForeignKey(publicacion_model, on_delete=models.CASCADE, related_name="Comentarios")
    body = models.TextField()
    publication_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['publication_date']

    def __str__(self):
        return 'Comentario {} by {}'.format(self.body, self.name)
