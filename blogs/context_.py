from blogs.models import Categoria


def categorias_(request):
    categorias = Categoria.objects.all()
    return {
        'categorias':categorias
    }
