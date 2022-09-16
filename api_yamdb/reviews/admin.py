from django.contrib import admin

from reviews.models import Comment, Review, Title


@admin.register(Title)
class TitleAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'year')


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('pk', 'text', 'author', 'title', 'score')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('pk', 'author', 'review', 'text')
