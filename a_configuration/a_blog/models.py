from django.db import models
from ckeditor.fields import RichTextField



class Blog(models.Model):
    title = models.CharField('Заголовок поста', max_length=100)
    text_blog = RichTextField(blank=True, null=True)
    author = models.CharField('Имя автора', max_length=50)
    date = models.DateField('дата поста')
    img = models.ImageField('Изображения', upload_to='image_blog/%Y')#папка в которой хранятся изображения

    class Meta:
        verbose_name = 'Запись' #читаемое человеком имя поля
        verbose_name_plural = 'Записи' # тоже самое но во множественном числе


    def __str__(self):
        return f'{self.title}, {self.author}, {self.date}'
