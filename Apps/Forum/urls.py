from django.urls import path

#Views Imports
from .views import MainThreads


urlpatterns = [
    path('Main_Threads/', MainThreads.as_view(), name='home')
]
