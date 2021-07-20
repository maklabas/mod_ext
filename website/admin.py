from django.contrib import admin

from website.models import Tag, Post, Author, Category

admin.site.register(Tag)
admin.site.register(Post)
admin.site.register(Author)
admin.site.register(Category)
