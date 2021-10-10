from django.db import models

# Create your models here.
class Tag(models.Model):
    name = models.CharField(max_length=256, verbose_name='작성자')
    
    register_date = models.DateTimeField(auto_now_add=True, verbose_name='작성일')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'stagram_tag'
        verbose_name = '태그'
        verbose_name_plural = '태그'
