from django.db import models

class Portfolio(models.Model):
    title = models.CharField('Заголовок поста', max_length=150)
    price = models.CharField('цена', max_length=20)
    text = models.TextField('Текст записи')
    img = models.ImageField('Изображения', upload_to='images/portfolio')#папка в которой хранятся изображения

    class Meta:
        verbose_name = 'Запись' #читаемое человеком имя поля
        verbose_name_plural = 'Записи' #тоже самое но во множественном числе


    def __str__(self):
        return f'{self.title}, {self.img}, {self.text}, {self.price}'