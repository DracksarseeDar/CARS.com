from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название категории")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"



class Tour(models.Model):
    title = models.CharField(max_length=200, verbose_name="Название тура")
    description = models.TextField(verbose_name="Описание")
    categories = models.ManyToManyField(Category, related_name="tours", verbose_name="Категории")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Тур"
        verbose_name_plural = "Туры"



class Booking(models.Model):
    person_name = models.CharField(max_length=100, verbose_name="ФИО туриста")
    tour = models.OneToOneField(Tour, on_delete=models.CASCADE, verbose_name="Тур")
    date = models.DateField(verbose_name="Дата поездки")

    def __str__(self):
        return f"{self.person_name} -> {self.tour.title}"

    class Meta:
        verbose_name = "Бронирование"
        verbose_name_plural = "Бронирования"



class Review(models.Model):
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE, related_name="reviews", verbose_name="Тур")
    author = models.CharField(max_length=100, verbose_name="Автор отзыва")
    text = models.TextField(verbose_name="Текст отзыва")
    rating = models.PositiveSmallIntegerField(default=5, verbose_name="Оценка")

    def __str__(self):
        return f"Отзыв от {self.author} на {self.tour.title}"

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"