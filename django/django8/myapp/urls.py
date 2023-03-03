from django.urls import path
from .views import fnTestGetQuery,fnTestPutPath,fnTestPostBody,fnTestDelHeader
urlpatterns = [
    path('test-query', fnTestGetQuery),
    path('test-path/<name>/<loc>', fnTestPutPath),
    path('test-body', fnTestPostBody),
    path('test-headers',fnTestDelHeader)
]