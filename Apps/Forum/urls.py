from django.urls import path

#Views Imports
from .views import *


urlpatterns = [
    path('Main_Threads/', CR_Threads.as_view(), name='home'),
    path('thread_<str:title>/thread_num_<int:pk>/', R_Thread.as_view(), name= 'read'),
    path('Update_Thread_<int:pk>/', U_Thread.as_view(), name='update'),
    path('deleting_<int:pk>/', D_Thread.as_view(), name='delete'),

]
