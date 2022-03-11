from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import View, UpdateView, DeleteView 
from django.urls import reverse_lazy

from .forms import Add_Thread_F
from .models import Post



# CRUD FOR THREADS VIEWS

class CR_Threads(View):
    def get(self, request, *args, **kwargs):
        last_threads = Post.objects.all()
        form = Add_Thread_F()

        context ={
            'threads': last_threads,
            'form': form
        }
        return render(request, 'Forum/threads.html', context)

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            form = Add_Thread_F(request.POST)
            if form.is_valid():
                title = form.cleaned_data.get('title')
                content = form.cleaned_data.get('content')

                p, created = Post.objects.get_or_create(title=title, content=content)
                try:
                    p.save()
                    return redirect('Forum:home')
                except:
                    #FALTA AGREGAR UNA ALERTA CON JS O CSS PARA SEñALAR AL USUARIO QUE NO SE CREO SU POST
                    return redirect('Forum:home')
            context = {}
            return render(request, 'Forum:new', context)


class R_Thread(View):
    def get(self, request, pk, *args, **kwargs):
        thread = get_object_or_404(Post, pk=pk)
        context = {'post':thread}
        return render(request, 'Forum/thread.html', context)


class U_Thread(UpdateView):
    model = Post
    fields = ['title', 'content']
    template_name = 'Forum/u_thrd.html'

    def get_success_url(self):
        pk = self.kwargs['pk']
        return reverse_lazy('Forum:home')

class D_Thread(DeleteView):
    model = Post
    template_name = 'Forum/d_thrd.html'
    success_url = reverse_lazy('Forum:home')




