from django.db import models


# 创建模型
class Topic(models.Model):
    """用户学习主题"""
    text = models.CharField(max_length=2000)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text


class Entry(models.Model):
    """学到的相关的某个主题的知识"""
    topic = models.ForeignKey(Topic)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'

        def __str__(self):
            return self.text[:50] + "..."
