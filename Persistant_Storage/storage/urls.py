from django.urls import path
from . import views

urlpatterns = [
    path('user', views.create_user, name='create_user'),
    path('user/<str:uid>', views.user_data, name='user_data'),
    path('users', views.all_users, name='all_users')
]