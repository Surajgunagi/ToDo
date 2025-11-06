from django.urls import path
from . import views

urlpatterns = [
    # add task
    path('add_Task/', views.add_Task, name='add_Task'),
    # mark as done
    path('mark_as_done/<int:pk>/', views.mark_as_done, name='mark_as_done'),
    # mark as undone
    path('mark_as_undone/<int:pk>/', views.mark_as_undone, name='mark_as_undone'),
    # edit features
    path('edit_task/<int:pk>/', views.edit_task, name='edit_task'),
    # delete task
    path('delete_task/<int:pk>/', views.delete_task, name='delete_task'),
]