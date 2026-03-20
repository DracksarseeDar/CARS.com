from django.db import models
from django.contrib.auth.models import User

class CustomUser(User):
    phone_number = models.CharField(max_length=20, default='+996') 
    city = models.CharField(max_length=100)
    
    GENDER = (
        ('MALE', 'MALE'),
        ('FEMALE', 'FEMALE')
    )
    gender = models.CharField(max_length=100, choices=GENDER, default='MALE')

    photo = models.ImageField(upload_to='users/')
    github_link = models.URLField(blank=True)
    experience_years = models.PositiveIntegerField(default=0)
    specialization = models.CharField(max_length=100)
    resume = models.FileField(upload_to='resumes/', blank=True)
    linkedin = models.URLField(blank=True)
    birth_date = models.DateField(null=True, blank=True)
    skills_description = models.TextField(blank=True)

    def __str__(self):
        return self.username 