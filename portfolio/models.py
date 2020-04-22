from django.db import models

class Project(models.Model):
    title= models.CharField(max_length=10000)
    description= models.TextField()
    image=models.ImageField(upload_to='portfolio/images/', blank=True)
    url=models.URLField(blank=True)
    technology= models.CharField(max_length=10000)
  
    projectTypeList = (
        ('MachineLearning', 'MachineLearning'),
        ('DataAnalytics', 'DataAnalytics'),
        ('DeepLearning', 'DeepLearning'))
    typeProject = models.CharField(max_length=200, choices=projectTypeList)
    def __str__(self):
        return self.title

class WorkExperience(models.Model):
    role= models.CharField(max_length=20)
    company=models.CharField(max_length=20)
    description= models.TextField()
    placeCity=models.CharField(max_length=20)
    placeCountry=models.CharField(max_length=20)
    dateStart= models.DateField()
    dateEnd= models.DateField()

    class Meta:
        ordering = ['-dateEnd']


    def __str__(self):
        return self.role

class Education(models.Model):
    title= models.CharField(max_length=100)
    school=models.CharField(max_length=20)
    description= models.TextField()
    placeCity=models.CharField(max_length=20)
    placeCountry=models.CharField(max_length=20)
    dateStart= models.DateField()
    dateEnd= models.DateField()
    finalProject=models.CharField(max_length=100)

    class Meta:
        ordering = ['-dateEnd']

    def __str__(self):
        return self.title


class Skill(models.Model):
    title= models.CharField(max_length=20)
    description= models.TextField()
    level=models.CharField(max_length=20)

    def __str__(self):
        return self.title

class OtherSkill(models.Model):
    title= models.CharField(max_length=20)

    def __str__(self):
        return self.title

