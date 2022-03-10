
from django.contrib import admin
from django.urls import path, include
from argparse import Namespace
from Apps.HomePage import views as hpv


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', hpv.HomePage.as_view(), name='Home'),
    path('forum/', include(('Apps.Forum.urls', 'Apps.Forum'), namespace='Forum')),
]
