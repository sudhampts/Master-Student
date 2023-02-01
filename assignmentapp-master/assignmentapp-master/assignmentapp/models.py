from django.db import models


# Create your models here.
class Student(models.Model):
    Name = models.CharField(max_length=40)
    UserNAme = models.CharField(max_length=40)
    Password = models.CharField(max_length=30)

    def __str__(self):
        return f'{self.Name}'


class Master(models.Model):
    Name = models.CharField(max_length=40)
    UserNAme = models.CharField(max_length=40)
    Password = models.CharField(max_length=30)


class Task(models.Model):
    Left = models.CharField(max_length=20)
    Right = models.CharField(max_length=20)
    Operator = models.CharField(max_length=30)
    Complete = models.BooleanField(default=False)
    Student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
