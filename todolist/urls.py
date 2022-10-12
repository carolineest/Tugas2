from django.urls import path
from todolist.views import *

app_name = 'todolist'

urlpatterns = [
    path('', show_todolist, name='show_todolist'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('create-task/', create_task, name='create-task'),
    path('status/<int:id>', ubah_status, name='ubah_status'),
    path('hapus/<int:id>', hapus_task, name='hapus_task'),
    path('json/', show_json, name='show_json'),
    path('add/', add_ajax, name='add_ajax'),
    path('delete/<int:id>/', delete_ajax, name='delete_ajax'),
]