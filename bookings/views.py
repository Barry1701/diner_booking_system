from django.shortcuts import render
from django.views import generic
from .models import Menu

class MenuView(generic.ListView):
    template_name = 'menu_piast.html'
    queryset = Menu.objects.all()
    context_object_name = 'menu_items'
