from django.shortcuts import render
from django.views import View

#HOME PAGE VIEW

class HomePage(View):
    def get(self, request, *args, **kwargs):
        context = {

        }
        return render(request, 'Home/index.html', context)
