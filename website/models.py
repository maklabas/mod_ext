from django.db import models
from django.db.models import PROTECT, DO_NOTHING, SET_NULL, CASCADE


class Tag(models.Model):
    tag_name = models.CharField(max_length=40, verbose_name='имя тега', null=False, blank=False, unique=True,
                                default='tag')


class Author(models.Model):
    surname = models.CharField(max_length=60, verbose_name='фамилия')
    login = models.CharField(max_length=40, verbose_name='логин')
    name = models.CharField(max_length=60, verbose_name='имя')

    class Meta:
        verbose_name = "Автор"
        verbose_name_plural = "Авторы"

    def __str__(self):
        return self.login


class Category(models.Model):
    name = models.CharField(max_length=60, verbose_name='имя категории')

    def __str__(self):
        return self.name


class Post(models.Model):
    post_name = models.CharField(max_length=60, verbose_name='имя поста', blank=False, null=False, default='new post')
    description = models.CharField(max_length=120, verbose_name='описание')
    created = models.DateField(auto_now_add=True, verbose_name='создан', blank=True, null=True)
    changed = models.DateField(auto_now=True, verbose_name='изменен', blank=True, null=True)
    if_published = models.BooleanField(default=False, verbose_name='опубликован ли')
    tag = models.ManyToManyField(Tag)
    category = models.ForeignKey(Category, null=True, on_delete=models.CASCADE, verbose_name='категория')
    author = models.ForeignKey(Author, null=True, on_delete=models.CASCADE, verbose_name='автор')
