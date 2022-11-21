from django.urls import path
from . import views

app_name = 'board'

urlpatterns = [
    path('', views.board_list, name='list'),
    path('<int:board_id>/', views.board_view, name='view'),
    path('add', views.board_add, name='add'),
]