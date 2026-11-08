# VISTAS de la app schoolmanagement.
# Una vista recibe la peticion del navegador y devuelve una respuesta (HTML).
# Aqui usamos VISTAS BASADAS EN CLASES (CBV): Django ya trae el comportamiento
# programado; nosotros solo le decimos QUE MODELO usar y QUE PLANTILLA rellenar.

# ListView = "lista de todas las filas"; DetailView = "una sola fila por su id".
from django.views.generic import DetailView, ListView

# Importamos el modelo para decirle a las vistas de que tabla leer.
from schoolmanagement.models import School

# __all__ = los nombres "publicos" de este archivo (lo que exporta).
__all__ = [
    "SchoolDetailView",
    "SchoolListView",
]


# Lista de TODAS las escuelas (equivale a School.objects.all()).
# Hereda de ListView: "(ListView)" significa "es un tipo de ListView".
class SchoolListView(ListView):
    # De que tabla saca los datos.
    model = School
    # Que plantilla rellena. A la plantilla le pasa la lista con el nombre
    # "object_list" (y tambien "school_list").
    template_name = "schoolmanagement/school_list.html"


# Detalle de UNA escuela. Django la busca por el "pk" (el id) que viene en la URL,
# por ejemplo /school/2/ -> la escuela con id 2. Si no existe, responde 404.
class SchoolDetailView(DetailView):
    model = School
    # A la plantilla le pasa la escuela con el nombre "object" (y tambien "school").
    template_name = "schoolmanagement/school_detail.html"
