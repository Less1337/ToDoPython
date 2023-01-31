from django.urls import path
from .views import *

urlpatterns = [
#    path('task/<int:taskid>/', task),
    path('', index, name='index'),
    path('add', addtask, name='add'),
    path('complete/<int:task_id>/', complete, name='complete'),
    path('delete/<int:task_id>/', delete, name='delete'),
]

