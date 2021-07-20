from django.shortcuts import render

from website.models import Post


def index(request):
    context = {
        # https://coderoad.ru/55237205/Как-получить-все-значения-для-определенного-поля-в-django-ORM
        # не сортировалось номерам записей. Метод order_by мне в этом помог
        'posts': Post.objects.values_list('id', flat=True).order_by('-id'),
    }
    return render(request, 'blog/index.html', context=context)


def details(request, pk=None):
    context = {
        'post': Post.objects.get(pk=pk),
    }
    return render(request, 'blog/post.html', context=context)


def create(request):
    context = {}
    return render(request, 'blog/create.html', context=context)
