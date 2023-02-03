from django.db import models


class User(models.Model):
    name=models.CharField(max_length=120,verbose_name='Имя')
    second_name= models.CharField(max_length=120, verbose_name='Фамилия')
    date_of_birth= models.DateField(verbose_name='Дата рождения')
    country=models.CharField(max_length=120,verbose_name='Страна')

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name='Пользователь'
        verbose_name_plural='Пользователи'

class Post (models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE,related_name='Пост')
    text= models.CharField(max_length=120, verbose_name='Текст')
    image=models.ImageField(upload_to="image/",null=True,blank=True)
    create_at=models.DateField( auto_now=True, verbose_name='Дата создания')

    def __str__(self) -> str:
        return self.text
        
    
    class Meta:
        verbose_name="Пост"
        verbose_name_plural="Посты"
