# coding: utf-8
from django.shortcuts import render, get_object_or_404
from .models import Review, Wine

# Create your views here.
def review_list(request):
    # order_by QuerySet 根据模型Meta 类的ordering 选项排序
    # - 降序排序
    # 隐式的是升序排序。若要随机排序，请使用"?"
    # pub_date最大的9条
    latest_review_list = Review.objects.order_by('-pub_date')[:9]
    # 添加到模板上下文的一个字典
    context = {'latest_review_list':latest_review_list}
    return render(request, 'reviews/review_list.html', context)


def review_detail(request, review_id):
    # 调用django 的get方法，如果查询的对象不存在的话，会抛出一个DoesNotExist的异常
    # The following example gets the object with the primary key of review_id from Review
    review = get_object_or_404(Review, pk=review_id)
    return render(request, 'reviews/review_detail.html', {'review': review})


def wine_list(request):
    wine_list = Wine.objects.order_by('-name')
    context = {'wine_list':wine_list}
    return render(request, 'reviews/wine_list.html', context)

def wine_detail(request, wine_id):
    wine = get_object_or_404(Wine, pk=wine_id)
    return render(request, 'reviews/wine_detail.html', {'wine':wine})