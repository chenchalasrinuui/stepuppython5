from django.urls import path
from .views import fnDeleteUser,fnGetUsers,fnSaveUser,fnUpdateUser
urlpatterns = [
    path('get-users', fnGetUsers),
    path('save-user',fnSaveUser),
    path('del-user',fnDeleteUser),
    path('update-user',fnUpdateUser)
]