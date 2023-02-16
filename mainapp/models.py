from django.db import models
from django.contrib.auth import get_user_model
User= get_user_model()




class Post (models.Model):
    owner=models.ForeignKey(User, on_delete=models.CASCADE,related_name='Пост')
    text= models.CharField(max_length=120, verbose_name='Текст')
    image=models.ImageField(upload_to="image/",null=True,blank=True)
    create_at=models.DateField( auto_now_add=True, verbose_name='Дата создания')
    like= models.PositiveIntegerField(default=0)
    dislike=models.PositiveIntegerField(default=0,)

    def __str__(self) -> str:
        return self.text
        
    
    class Meta:
        verbose_name="Пост"
        verbose_name_plural="Посты"


class Like(models.Model):

    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='likes')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:

        verbose_name = "Лайки"
        verbose_name_plural = "Лайк"

    def __str__(self):
        return f"{self.author} -- {self.post.text} -- {self.created_at}"

class DisLikes(models.Model):

    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='dislikes')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:

        verbose_name = "Дизлайки"
        verbose_name_plural = "Дизлайк"

    def __str__(self):
        return f"{self.author} -- {self.post.text} -- {self.created_at}"