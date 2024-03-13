from django.db import models

# Create your models here.

class Pets(models.Model):
    gender_option = (("Male","Male"),("Female","Female"))

    name =models.CharField(max_length=30)
    species =models.CharField(max_length=30)
    breed = models.CharField(max_length=30)
    age = models.IntegerField()
    gender = models.CharField(max_length=20,choices=gender_option)
    image = models.ImageField(upload_to='media')
    description = models.TextField(max_length=1000)


class Student(models.Model):
    student_name = models.CharField(max_length=120)
    student_age = models.IntegerField()
    student_email = models.EmailField()
    student_course = models.CharField(max_length=100)

class Author(models.Model):
    author_name=models.CharField(max_length=100)

class Book(models.Model):
    title=models.CharField(max_length=100)
    author=models.ForeignKey(Author,on_delete=models.CASCADE)