from django.shortcuts import render
from django.http import HttpResponse
from blogs.models import *
from django.views import generic
from django.utils import timezone
from django.db.models import Q
# Create your views here.

def inicio(request):
    posts = Post.objects.filter(
        pub_date__lte=timezone.now()
    )
    categorias = Categoria.objects.all()
    featured = Post.objects.filter(featured=True).filter(
        pub_date__lte=timezone.now()
    )[:3] 


    context = {
        'post_list':posts,
        'categorias':categorias,
        'featured':featured,

    }
    return render(request, 'blogs/inicio.html',context=context)

class PostDetailView(generic.DetailView):
    model = Post
    queryset = Post.objects.filter(
        pub_date__lte=timezone.now() 
    )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categorias'] = Categoria.objects.all()
           
        return context

class FeaturedListView(generic.ListView):
    model = Post
    template_name= 'blogs/resultados.html'

    def get_queryset(self):
        query = Post.objects.filter(feature=True).filter(
        pub_date__lte=timezone.now() )

        return query

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categorias'] = Categoria.objects.all()
           
        return context

class CategoryListView(generic.ListView):
    model = Post
    template_name = 'blogs/resultados.html'

    def get_queryset(self):
        query = self.request.path.replace('/categorias/','')
        print(query)
        post_list = Post.objects.filter(categorias__slug=query).filter(
        pub_date__lte=timezone.now() )

        return post_list

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categorias'] = Categoria.objects.all()
           
        return context        

class SearchListView(generic.ListView):
    model = Post
    template_name = 'blogs/resultados.html'

    def get_queryset(self):
        query = self.request.GET.get('search')
        print(query)
        post_list = Post.objects.filter(
            Q(titulo__icontains=query) | Q(categorias__titulo__icontains=query)
        ).filter(
        pub_date__lte=timezone.now()).distinct()

        return post_list

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categorias'] = Categoria.objects.all()
           
        return context        
        
