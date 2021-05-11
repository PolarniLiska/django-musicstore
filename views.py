from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import *
def index(request):

    return render(request, template_name='index.html')

class DeskaListView(ListView):
    model = Deska
    context_object_name = 'deska'
    template_name = 'list.html'

class DeskaDetailView(DetailView):
    model = Deska
    context_object_name = 'deska'
    template_name = 'detail.html'
