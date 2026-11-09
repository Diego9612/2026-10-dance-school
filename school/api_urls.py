from django.urls import path

from school import api_views

urlpatterns = [
    path(route="courses/", view=api_views.CourseListAPI.as_view(), name="api_course_list"),
    path(route="courses/new/", view=api_views.CourseCreateAPI.as_view(), name="api_course_create"),
    path(route="courses/<int:pk>/", view=api_views.CourseDetailAPI.as_view(), name="api_course_detail"),
    path(route="courses/<int:pk>/edit/", view=api_views.CourseUpdateAPI.as_view(), name="api_course_update"),
    path(route="courses/<int:pk>/delete/", view=api_views.CourseDestroyAPI.as_view(), name="api_course_delete"),
]