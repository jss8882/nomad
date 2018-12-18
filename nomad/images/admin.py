from django.contrib import admin

from . import models


@admin.register(models.Image)
class ImageAdmin(admin.ModelAdmin):
    #지역정보를 클릭함으로써 이미지 편집을 할수 있음
    list_display_links = (
        'location',
    )
    #로케이션을 검색학수 있는 창이 생김
    search_fields = (
        'location',
    )
    
    list_filter = (
        'location',
        'creator'
    )
    
    list_display = (
        'created_at',
        'updated_at',
        'file',
        'location',
        'caption',
        'creator'
    )

@admin.register(models.Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = (
        'creator',
        'image',
        'created_at',
        'updated_at'
    )

@admin.register(models.Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = (
        'message',
        'creator',
        'image',
        'created_at',
        'updated_at'
    )
# Register your models here.
