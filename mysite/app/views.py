from django.shortcuts import render
from django.views.generic import ListView

from .models import Pictures


class Main(ListView):
    model = Pictures
    # Поле, которое будет использоваться для сортировки объектов
    ordering = 'header'
    # Указываем имя шаблона, в котором будут все инструкции о том,
    # как именно пользователю должны быть показаны наши объекты
    template_name = 'main.html'
    # Это имя списка, в котором будут лежать все объекты.
    # Его надо указать, чтобы обратиться к списку объектов в html-шаблоне.
    context_object_name = 'main'

