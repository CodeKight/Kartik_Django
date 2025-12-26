from django.db import models

# Create your models here.


from django.db import models


class Info(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    contact = models.TextField()
    education = models.TextField()
    hobbies = models.TextField()
    skills = models.TextField()


class Education(models.Model):
    degree = models.CharField(max_length=100)
    institution = models.CharField(max_length=150)
    year_of_passing = models.IntegerField()
    percentage = models.FloatField()


class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    techstack = models.CharField(max_length=200)
    link = models.URLField()

   




# Portfolio
# User: name, email, phone, contact, education, hobbies, skills

# Education: degree, institution, year_of_passing, percentage

# projects :  title, description, techstack ,Link