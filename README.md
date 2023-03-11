# Proyecto-Final-Adorno
Proyecto Final Coder House - Python

Comisión 34665

Alumno: Agustín Andrés Adorno

VERSION  BRANCH V1.6.1



Descripcion del Proyecto
Blog dedicado a la publicacion de noticias

A fin de navegar por las secciones de la página web, el usuario será requerido iniciar sesión o registrarse en caso de no contar con usuario o contraseña. 
En ambas opciones, una vez la página valide la autenticación del usuario, este será redirigido al inicio de la página web.

Dentro de este sitio, el usuario podra ver y realizar:
1.visualizar articulos creados por otros usuarios.
2.Crear sus propios articulos con imagenes (PROXIMAMENTE)
3.Filtrar los articulos que desea ver o buscar palabras clave de los articulos.
4.Dentro de los articulos, cada usuario podra dejar un comentario.
5.En la seccion de destacados podra visualizar 3 articulos diferentes y si sigue bajando, aparecera un boton para cambiar a la pagina siguiente.
6.Hacer sign in, login, logout y en caso de ser necesario resetear una contraseña.
7.el usuario podra editar la informacion del perfil (PROXIMAMENTE)

PROGRAMAS UTILIZADOS PARA LA FUNCIONALIDAD DEL BLOG
bootstrap==5.2
asgiref==3.6.0
crispy-bootstrap5==0.7
Django==4.1.7
django-crispy-forms==2.0
Markdown==3.4.1
Pillow==9.4.0
sqlparse==0.4.3
tzdata==2022.7

REQUERIMIENTO PARA ARRANCAR EL PROYECTO:

VIDEO DEMOSTRATIVO: https://youtu.be/Y2m40pZdYQ4

pip install -r requirements.txt

pipenv shell

python manage.py runserver