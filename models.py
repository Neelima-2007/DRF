from django.db import models

# Create your models here.

class Student(models.Model):
    student_id = models.IntegerField()
    student_name = models.CharField(max_length=55)
    student_branch = models.CharField(max_length=10)

    def __str__(self):
        # my name is neelima
        return f"{self.student_id},{self.student_name},{self.student_branch}"