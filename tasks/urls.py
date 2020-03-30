from django.urls import path
from .views import (
    index, 
    task_update_view, 
    task_delete_view,
    cross_out_item_view,
    uncross_item_view,
)

urlpatterns = [
    path('<int:pk>/cross_out/', cross_out_item_view, name='task_cross'),
    path('<int:pk>/uncross/', uncross_item_view, name='task_uncross'),
    path('<int:pk>/edit/', task_update_view, name='task_edit'),
    path('<int:pk>/delete/', task_delete_view, name='task_delete'),
    path('', index, name='home'),
]