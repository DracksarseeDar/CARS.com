from django import forms
from . import models
from django.contrib.auth.forms import UserCreationForm
from captcha.fields import CaptchaField
GENDER = (
        ('MALE', 'MALE'),
        ('FEMALE', 'FEMALE')
    )


class CustomRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    photo = forms.ImageField(required=True)
    phone_number = forms.CharField(max_length=20 , initial='+996', required=True)
    gender = forms.ChoiceField(choices=GENDER, required=True)
    city = forms.CharField(max_length=100, required=True)

    github_link = forms.URLField(required=False, label="GitHub")
    experience_years = forms.IntegerField(initial=0, label="Стаж")
    specialization = forms.CharField(max_length=100, label="специализация ")
    resume = forms.FileField(required=False, label="Резюме")
    linkedin = forms.URLField(required=False)
    birth_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), label="Дата рождения")
    skills_description = forms.CharField(widget=forms.Textarea, label="О себе")
    
    captcha = CaptchaField(label="Введите текст с картинки")
    
    class Meta:
        model = models.CustomUser
        fields = (
            "username", "first_name", 
            "last_name", "email", 
            "phone_number", "gender", 
            "city", "photo",
            "github_link", "experience_years", 
            "specialization", 
            "resume", "captcha" 
        )
    
    def save(self, commit=True):
        
        user = super(CustomRegisterForm, self).save(commit=False)
        
        
        user.phone_number = self.cleaned_data.get('phone_number')
        user.city = self.cleaned_data.get('city')
        user.gender = self.cleaned_data.get('gender')
        user.experience_years = self.cleaned_data.get('experience_years')
        user.specialization = self.cleaned_data.get('specialization')
        user.photo = self.cleaned_data.get('photo')
        user.resume = self.cleaned_data.get('resume')
        user.github_link = self.cleaned_data.get('github_link')
        user.birth_date = self.cleaned_data.get('birth_date')
        user.skills_description = self.cleaned_data.get('skills_description')

       
        if commit:
            user.save()
        return user