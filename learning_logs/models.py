from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Topic(models.Model):
    """用户学习主题"""
    text = models.CharField(max_length=2000)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)  # 建立外键

    def __str__(self):
        """返回模型的字符串表示"""
        return self.text


class Entry(models.Model):
    """学到有关某个主题的具体知识"""
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)  # 建立外键
    text = models.TextField(max_length=2000)  #
    date_added = models.DateTimeField(auto_now_add=True)  # 自动创建条目时间戳

    class Meta:
        verbose_name_plural = "entries"  # 储管理模型存额外的信息

    def __str__(self):
        """返回模型字符串表示"""
        if len(self.text) > 50:
            return self.text[:50] + "..."  # 显示前50个字符
        return self.text
