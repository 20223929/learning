from django import forms

from .models import Topic, Entry


class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['text']
        labels = {'text': ''}


class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['text']
        # 给text字段指定一个空标签
        labels = {'text': ''}
        # 覆盖默认值的小部件，单行文本框/多行文本区域/下拉列表
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}
