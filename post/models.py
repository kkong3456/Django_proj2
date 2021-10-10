from django.db import models
from tag.models import Tag
from dsuser.models import Dsuser

# Create your models here.

class Post(models.Model):
    name = models.ForeignKey('dsuser.Dsuser',on_delete=models.CASCADE,max_length=256, verbose_name='작성자')
    img_url = models.CharField(max_length=256,verbose_name='이미지주소')
    contents = models.TextField(verbose_name='내용')
    tag = models.ManyToManyField('tag.Tag',verbose_name='태그')
    register_date = models.DateTimeField(auto_now_add=True, verbose_name='작성일')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'stagram_post'
        verbose_name = '게시글'
        verbose_name_plural = '게시글'


