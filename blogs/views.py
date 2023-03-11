from django.shortcuts import render
from django.http import HttpResponse
from blogs.models import *
from django.views import generic, View
from django.utils import timezone
from django.db.models import Q
from django.views.generic.detail import SingleObjectMixin
from django.views.generic import FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from blogs.forms import *
from django.urls import reverse
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView

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
        context['form'] = PostCommentForm()
        return context

class PostCommentFormView(LoginRequiredMixin, SingleObjectMixin, FormView):
    template_name = 'blogs/post_detail.html'
    form_class = PostCommentForm
    model = Post

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().post(request, *args, **kwargs)
    
    def form_valid(self, form):
        f = form.save(commit=False)
        f.author = self.request.user
        f.post = self.object
        f.save()
        return super().form_valid(form)
    
    def get_success_url(self):



        return reverse('blogs:post', kwargs={'slug': self.object.slug})+ '#comments-section'  



class PostView(View):

    def get(self, request, *args, **kwargs):
        view = PostDetailView.as_view()
        return view(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):   
        view = PostCommentFormView.as_view()
        return view(request, *args, **kwargs)    


class FeaturedListView(generic.ListView):
    model = Post
    template_name = 'blogs/resultados.html'
    paginate_by = 3 

    def get_queryset(self):
        query = Post.objects.filter(featured=True).filter(
        pub_date__lte=timezone.now() )

        return query



class CategoryListView(generic.ListView):
    model = Post
    template_name = 'blogs/resultados.html'
    paginate_by = 2

    def get_queryset(self):
        query = self.request.path.replace('/categorias/','')
        print(query)
        post_list = Post.objects.filter(categorias__slug=query).filter(
        pub_date__lte=timezone.now() )

        return post_list

   

class SearchListView(generic.ListView):
    model = Post
    template_name = 'blogs/resultados.html'
    paginate_by = 2

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
        context['query'] = self.request.GET.get('search')
           
        return context

class CrearPost(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostCreationForm
    success_url = reverse('inicio')
    template_name = 'blogs/crear_post.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(CrearPost, self).form_valid(form)



