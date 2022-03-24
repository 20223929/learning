from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render

# Create your views here.
from django.urls import reverse

from .forms import TopicForm, EntryForm
from .models import Topic, Entry


def index(request):
    """学习笔记主页"""
    return render(request, 'learning_logs/index.html')


# 注解 只允许已登录的用户
@login_required
def topics(request):
    """显示所有主题"""
    topics = Topic.objects.filter(owner=request.user).order_by('date_added')
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)


@login_required
def topic(request, topic_id):
    """显示特定主题及所有条目"""
    topic = Topic.objects.get(id=topic_id)
    # 确认请求的主题属于当前用户
    check_topic_owner(request, topic)

    entries = topic.entry_set.order_by('-date_added')
    # 页面可显示的数据
    context = {'topic': topic, 'entries': entries}
    return render(request, 'learning_logs/topic.html', context)


@login_required
def new_topic(request):
    """用于添加新主题"""
    if request.method != 'POST':
        # 未提交数据：创建一个空表单
        form = TopicForm()
    else:
        # POST提交的数据，对数据进行处理
        form = TopicForm(request.POST)
        if form.is_valid():
            new_topic = form.save(commit=False)
            new_topic.owner = request.user
            new_topic.save()
            return HttpResponseRedirect(reverse('learning_logs:topics'))
    # 页面可显示的数据
    context = {'form': form}
    return render(request, 'learning_logs/new_topic.html', context)


@login_required
def new_entry(request, topic_id):
    """用于在特定的主题中添加新条目"""
    topic = Topic.objects.get(id=topic_id)

    if request.method != 'POST':
        # 未提交数据，创建一个空表单
        form = EntryForm()
    else:
        # POST提交数据，对数据进行处理
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return HttpResponseRedirect(reverse('learning_logs:topic', args=[topic.id]))
    # 页面可显示的数据
    context = {'topic': topic, 'form': form}
    return render(request, 'learning_logs/new_entry.html', context)


@login_required
def edit_entry(request, entry_id):
    """用于修改特定条目信息"""
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic
    # 检查是否是当前用户
    check_topic_owner(request, topic)

    if request.method != 'POST':
        # 除此请求，使用当前条目填充表单
        form = EntryForm(instance=entry)
    else:
        # POST提交数据，对数据进行处理
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("learning_logs:topic", args=[topic.id]))
    # 页面可显示的数据
    context = {'entry': entry, 'topic': topic, 'form': form}
    return render(request, "learning_logs/edit_entry.html", context)


def check_topic_owner(request, topic):
    """检查是否是当前登录用户"""
    if topic.owner != request.user:
        raise Http404
