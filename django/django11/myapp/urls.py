from django.urls import path
from .views import getUsers,saveUser
urlpatterns = [
    path('get-users', getUsers),
    path('save-user',saveUser)
]