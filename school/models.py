from django.db import models

# Create your models here.
from schoolmanagement.models import School

class DayOfTheWeek(models.Model):
    number = models.PositiveSmallIntegerField(unique=True)
    name = models.CharField(max_length=20)
    
    def __str__(self):
        return self.name
    
    
class Classroom(models.Model):
    capacity = models.PositiveIntegerField()
    name = models.CharField(max_length=50)
    
    
    def __str__(self):
        return self.name
    
    
class Course(models.Model):
    subject = models.CharField(max_length=100)
    day_of_the_week = models.ForeignKey(
        DayOfTheWeek, on_delete=models.PROTECT, related_name="courses"
    )
    starting_hour = models.TimeField()
    classroom = models.ForeignKey(
        Classroom, on_delete=models.PROTECT, related_name="courses"
    )
    school = models.ForeignKey(
        School, on_delete=models.CASCADE, related_name="courses"
    )

    def __str__(self):
        return f"{self.subject} - {self.day_of_the_week} {self.starting_hour}"