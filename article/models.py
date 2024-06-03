from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Article(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    content = RichTextField()
    created_date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='articles', blank=True, null=True)

    def __str__(self):
        return f'{self.title} | {self.author}'
