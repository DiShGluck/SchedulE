from django.db import models
from django.contrib.auth.models import User

class Group(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Subject(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    last_name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100)

    def __str__(self):
        initials = f"{self.first_name[0]}.{self.middle_name[0]}." if self.middle_name else f"{self.first_name[0]}."
        return f"{self.last_name} {initials}"

class Schedule(models.Model):
    day_shoices = [
        (1, "Понедельник"),
        (2, "Вторник"),
        (3, "Среда"),
        (4, "Четверг"),
        (5, "Пятница"),
        (6, "Суббота")
    ]

    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    day = models.IntegerField(choices= day_shoices) 
    start_time = models.TimeField(default='08:00')

    def __str__(self):
        return f"{self.group} {self.subject} {self.teacher} {self.get_day_display()} {self.start_time}"
