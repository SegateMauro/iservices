from django.shortcuts import render
from .models import Post


def home(request):
    lista = [
        'Django', 'Python', 'Git', 'Html', 
        'Banco de Dados', 'Linux', 'Nginex', 'Uwsgi',
        'Systemctl'    
    ]
    list_posts = Post.objects.all()

    data = {
        'name': 'Curso de Django 3',
        'lista_tecnologias': lista, 
        'posts': list_posts 
        }

    return render(request, 'index.html', data)
