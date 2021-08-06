# from django.db import models

# # Create your models here.

# class Skill(models.Model):
#     name = models.CharField(max_length=50)
    
#     def __str__(self):
#         return self.name

# class Person(models.Model):
#     skills = models.ManyToManyField(Skill, blank=True, null=True)
#     def __str__(self):
#         return str(self.skills)




from django.db import models
from sortedm2m.fields import SortedManyToManyField

class Skills(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return str(self.name)
class Achievement(models.Model):
    skills = SortedManyToManyField(Skills)  
