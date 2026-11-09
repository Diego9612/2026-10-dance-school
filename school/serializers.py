from rest_framework import serializers

from school.models import Course


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ["id", "subject", "starting_hour", "day_of_the_week", "classroom", "school"]