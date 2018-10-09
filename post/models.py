from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=64)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    content = models.TextField()

    #设置排序显示为反向
    class Meta:
        ordering = ['-created']
