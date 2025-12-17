from django.db import models


# Create your models here.
class Skill(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Project(models.Model):
    skills = models.ManyToManyField(Skill)
    name = models.CharField(max_length=200)
    desc = models.TextField()
    giturl = models.CharField(max_length=500, default="")

    
class Experience(models.Model):
    position_name = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    exp_type = models.CharField(max_length=200)
    desc = models.TextField()
    skills_dev = models.ManyToManyField(Skill)
    