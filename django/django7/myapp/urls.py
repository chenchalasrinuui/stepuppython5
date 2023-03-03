from django.urls import path
from . import views

urlpatterns = [
    path('test-query', views.fnQueryParams),
    path('test-path/<n>/<l>', views.fnPathParams),
    path('test-header',views.fnRequestHeaders),
    path('test-body',views.fnRequestBody)
]