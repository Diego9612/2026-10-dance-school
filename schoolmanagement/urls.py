from django.urls import path

from schoolmanagement import views

urlpatterns = [
    # /school/        → lista de todas las escuelas
    path(route="", view=views.SchoolListView.as_view(), name="school_list"),
    # /school/2/      → detalle de la escuela con id 2 (<int:pk> captura el número)
    path(route="<int:pk>/", view=views.SchoolDetailView.as_view(), name="school_detail"),
]