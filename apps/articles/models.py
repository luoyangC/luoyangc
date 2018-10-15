from django.db import models

from home.models import Base
from apps.users.models import UserProfile
from mdeditor.fields import MDTextField

# Create your models here.


class Category(Base):
    """
    用户自定义分类
    """
    title = models.CharField(max_length=100, verbose_name='分类标题')
    info = models.CharField(max_length=100, null=True, blank=True, verbose_name='描述')

    class Meta:
        verbose_name = '分类'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


class Article(Base):
    """
    文章
    """
    title = models.CharField(max_length=100, null=False, blank=False, verbose_name='文章标题')
    content = MDTextField(null=True, blank=True, verbose_name='文章内容')
    profile = models.TextField(null=True, blank=True, verbose_name='文章简介')
    image = models.ImageField(max_length=100, upload_to='image/article/%Y/%m',
                              null=True, blank=True, verbose_name='封面图')
    image_url = models.CharField(max_length=100, default='http://127.0.0.1:8000/media/image/article/default/0.png',
                                 verbose_name='封面图地址')
    update_time = models.DateTimeField(auto_now_add=True, verbose_name='更新时间')

    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, verbose_name='作者')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='分类')
    view_nums = models.IntegerField(default=0, verbose_name='浏览数')
    comment_nums = models.IntegerField(default=0, verbose_name='评论数')
    fav_nums = models.IntegerField(default=0, verbose_name='收藏数')
    like_nums = models.IntegerField(default=0, verbose_name='点赞数')
    is_banner = models.BooleanField(default=False, verbose_name='是否轮播')
    tags = models.CharField(max_length=100, null=True, blank=True, verbose_name='Tag标签')

    class Meta:
        verbose_name = '文章'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title
