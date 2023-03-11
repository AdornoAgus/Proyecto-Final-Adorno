from django.urls import path
from blogs import views

app_name = 'blogs'

urlpatterns = [
path('',views.inicio),
path('post/<slug:slug>', views.PostView.as_view(), name='post'),
path('featured/', views.FeaturedListView.as_view(), name='featured'),
path('categorias/<slug:slug>',views.CategoryListView.as_view(), name='categorias'),
path('search/',views.SearchListView.as_view(), name='search'),
path('crear/', views.CrearPost.as_view(), name='crear'),

]

