from django.db import models

class Cars(models.Model):
    name_car = models.CharField(max_length=50, verbose_name='укажите название машины')
    description = models.TextField(verbose_name='укажите описание машины')
    image = models.ImageField(upload_to='cars/', verbose_name='загрузите изображение')

    CATEGORY_CAR = (
    ('седан', 'седан'),
    ('хэтчбек', 'хэтчбек'),
    ('кроссовер', 'кроссовер'),
    ('внедорожник', 'внедорожник'),
    ('купе', 'купе'),
    ('кабриолет', 'кабриолет'),
    ('универсал', 'универсал'),
    ('минивэн', 'минивэн'),
    ('пикап', 'пикап'),
    ('спорткар', 'спорткар'),
    )

    category_car = models.CharField(max_length=100, choices=CATEGORY_CAR, 
                                     verbose_name='выберите категорию')
    
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name_car

    class Meta:
        verbose_name = 'машину'
        verbose_name_plural = 'машины'

        