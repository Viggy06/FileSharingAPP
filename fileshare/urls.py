from django.urls import path
from .views import *

urlpatterns = [
    path('', home),
    path('download/<uid>/', download),
    path('handle/', HandleFileUpload.as_view()),
]