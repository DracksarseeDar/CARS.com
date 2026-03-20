from django.db import models
from car_categories.models import Cars

class DriverModel(models.Model):
    name_driver = models.CharField(max_length=100 , verbose_name='Введите свое ФИО:')
    drive_license =models.BooleanField(default=False , verbose_name='У вас есть права (Да/Нет) ') 
    photo = models.ImageField(upload_to="drivers/" , verbose_name='Всатвьте фото')
    choices_car = models.ForeignKey(Cars , on_delete=models.CASCADE )
    data_birth = models.DateField(verbose_name='Введите дату рождения:')
    experience = models.PositiveIntegerField( verbose_name='Водительский стаж:')
    
    def __str__(self):
        return f'{self.name_driver}: {self.choices_car}'
    
 