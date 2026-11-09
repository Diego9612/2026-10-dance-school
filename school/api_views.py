from rest_framework import generics

from school.models import Course
from school.serializers import CourseSerializer


class CourseListAPI(generics.ListAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class CourseDetailAPI(generics.RetrieveAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class CourseCreateAPI(generics.CreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class CourseUpdateAPI(generics.UpdateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class CourseDestroyAPI(generics.DestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer