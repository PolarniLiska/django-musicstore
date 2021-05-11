from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('list', views.DeskaListView.as_view(), name='list'),
    path('detail/<int:pk>', views.DeskaDetailView.as_view(), name='detail'),
]