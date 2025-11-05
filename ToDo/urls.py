from django.urls import path
from . import views

urlpatterns = [
    path('addTask/', views.add_task, name='add_task'),
    path('done/<int:pk>/', views.mark_as_done, name='mark_as_done')]