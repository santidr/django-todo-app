from django.urls import path
from .views import index, task_update_view, task_delete_view

urlpatterns = [
    path('<int:pk>/edit/', task_update_view, name='task_edit'),
    path('<int:pk>/delete', task_delete_view, name='task_delete'),
    path('', index, name='home'),
]