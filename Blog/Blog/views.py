

from django.shortcuts import render, get_object_or_404

from apps.articulos.models import Articulo
from apps.categorias.models import Categoria


def Home(request):
    # Artículo destacado (si no hay, cae al más reciente)
    articulo_destacado = (
        Articulo.objects.filter(destacado=True).order_by("-creado").first()
        or Articulo.objects.order_by("-creado").first()
    )

    # Últimos 3, excluyendo el destacado para no repetir
    ultimos_articulos = (
        Articulo.objects.exclude(pk=getattr(articulo_destacado, "pk", None))
        .order_by("-creado")[:4]
    )

    es_moderador = (
        request.user.is_authenticated
        and request.user.groups.filter(name="Moderador").exists()
    )
    
    categorias = Categoria.objects.all()

    ctx = {
        "articulo_destacado": articulo_destacado,
        "ultimos_articulos": ultimos_articulos,
        "es_moderador": es_moderador,
         "categorias": categorias,
    }
    return render(request, "home.html", ctx)

def filtrar_por_categoria(request, categoria_id):
    categoria = get_object_or_404(Categoria, id=categoria_id)
    articulos = Articulo.objects.filter(categoria=categoria)

    categorias = Categoria.objects.all()  # para que el menú siga estando
    ctx = {
        "categoria_actual": categoria,
        "articulos": articulos,
        "categorias": categorias
    }
    return render(request, "articulos/listar.html", ctx)