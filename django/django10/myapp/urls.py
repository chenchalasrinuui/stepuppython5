from django.urls import path
from .views import fnGetUsers,fnSaveUser
urlpatterns = [
    path('get-users', fnGetUsers),
    path('save-user', fnSaveUser),
]