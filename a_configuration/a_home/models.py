from django.db import models
from ckeditor.fields import RichTextField



class News(models.Model):
    title = models.CharField('Заголовок поста', max_length=100)
    text_news = RichTextField(blank=True, null=True)
    date = models.DateField('дата поста')
    img = models.ImageField('Изображения', upload_to='image_news/%Y')

    class Meta:
        verbose_name = 'Запись'
        verbose_name_plural = 'Записи'


    def __str__(self):
        return f'{self.title}, {self.text_news}, {self.date}'




class About(models.Model):
    title = models.CharField('Заголовок', max_length=100)
    text_news = RichTextField(blank=True, null=True)
    img = models.ImageField('Изображения', upload_to='image_about/%Y')

    class Meta:
        verbose_name = 'O нас'
        verbose_name_plural = 'О нас'


    def __str__(self):
        return f'{self.title}, {self.text_news}, {self.img}'