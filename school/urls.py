from django.urls import path

from school import views

urlpatterns = [
    path(route="giorni/", view=views.DayOfTheWeekListView.as_view(), name="dayoftheweek_list"),
    path(route="giorni/<int:pk>/", view=views.DayOfTheWeekDetailView.as_view(), name="dayoftheweek_detail"),
    path(route="giorni/nuovo/", view=views.DayOfTheWeekCreateView.as_view(), name="dayoftheweek_create"),
    path(route="giorni/<int:pk>/modifica/", view=views.DayOfTheWeekUpdateView.as_view(), name="dayoftheweek_update"),
    path(route="classi/", view=views.ClassroomListView.as_view(), name="classroom_list"),
    path(route="classi/<int:pk>/", view=views.ClassroomDetailView.as_view(), name="classroom_detail"),
    path(route="corsi/", view=views.CourseListView.as_view(), name="course_list"),
    path(route="corsi/<int:pk>/", view=views.CourseDetailView.as_view(), name="course_detail"),
    path(route="corsi/nuovo/", view=views.CourseCreateView.as_view(), name="course_create"),
    path(route="corsi/<int:pk>/modifica/", view=views.CourseUpdateView.as_view(), name="course_update"),
    path(route="corsi/<int:pk>/elimina/", view=views.CourseDeleteView.as_view(), name="course_delete"),
]