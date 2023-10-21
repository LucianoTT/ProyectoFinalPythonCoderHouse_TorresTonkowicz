# Proyecto Final Coder House - Python
#### Comisión: 47770
#### Alumno: Luciano Nicolas Torres Tonkowciz

## Nombre del Proyecto
Blog Fitness

## Versión
1.0

## Descripción del Proyecto

Esta página web es un blog sobre estar en forma y todas las actividades relacionadas con ello. 
Los usuarios podrán realizar las siguiente funciones:
- Registrarse, hacer login y logout.
- La capacidad de editar tu avatar y otros datos.
- Datos como tu contraseña, username, mail y redes sociales.
- Crear publicaciones de blog, editarlas o borrarlas.
- Comentar en las publicaciones de otras personas.
- Capacidad de manejar los usuarios(y sus datos), blogs publicados y sus comentarios desde el admin.

notas:
- La opción de editar o borrar publicaciones solo está permitido para el autor o desde la página del admin.
- El navegador que yo utilice para probar fue Google Chrome en modo incógnito.

## Tecnología Utilizada

##### Front-End
- HTML 
- CSS 
- Javascript 
- Bootstrap 

##### Back-End
- Python 3.11.4
- Django 4.2.5

### Pasos para el testeo
- Descargar o clonar el repositorio en tu PC.
- Abrirlo con VisualStudioCode.
- Ubicarse en la carpeta de blog con la funcion "cd" y iniciar el servidor con python manage.py runserver.
- Abrir un navegador en modo incógnito y escribir este sitio web http://127.0.0.1:8000/
- Crear una cuenta tocando el dropdown arriba a la derecha donde dice "Guest" y luego register.
- Luego hacer login con los datos correctos.
- En la página de blogs se podrá crear una nueva publicación o publicar comentarios en lo ya publicado.
- Arriba a la derecha donde antes estaba "Guest" ahora saldrá tu nombre de usuario en el dropdown, al tocarlo aparecerán opciones.
- Podrás editar tu perfil con avatar, descripción, username y redes sociales. También en la otra opción podrás cambiar tu password.
- Para probar el admin se deberá crear un super user en visualstudiocode escribiendo en consola python manage.py createsuperuser
- Luego deberás escribir este link http://127.0.0.1:8000/admin/ en el cual te logearas con el superuser creado antes.
- Acá aparecerán varias categorías en las que podrás manejas a los usuarios registrados, sus perfiles(avatar), los blogs comentados y sus comentarios.

## Pruebas Realizadas

## Video Demostración
