# coding: utf-8
from django.contrib import admin
from .models import Wine, Review

# Register your models here.
class ReviewAdmin(admin.ModelAdmin):
    model = Review
    # 使用list_display 去控制哪些字段会显示在Admin 的修改列表页面中。
    list_display = ('wine', 'rating', 'user_name', 'comment', 'pub_date')
    # list_filter 设置激活激活Admin 修改列表页面右侧栏中的过滤器
    list_filter = ['pub_date', 'user_name']
    # search_fields 设置启用Admin 更改列表页面上的搜索框。此属性应设置为每当有人在该文本框中提交搜索查询将搜索的字段名称的列表。
    search_fields = ['comment']
    
admin.site.register(Wine)
admin.site.register(Review, ReviewAdmin)
