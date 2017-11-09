# coding: utf-8
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from .models import Review, Wine
from .forms import ReviewForm
import datetime

from django.contrib.auth.decorators import login_required

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
    form = ReviewForm()
    return render(request, 'reviews/wine_detail.html', {'wine': wine, 'form': form})


@login_required
def add_review(request, wine_id):
    wine = get_object_or_404(Wine, pk=wine_id)
    form = ReviewForm(request.POST)
    if form.is_valid():
        rating = form.cleaned_data['rating']
        comment = form.cleaned_data['comment']
        # user_name = form.cleaned_data['user_name']
        user_name = request.user.username
        review = Review()
        review.wine = wine
        review.user_name = user_name
        review.rating = rating
        review.comment = comment
        review.pub_date = datetime.datetime.now()
        review.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('reviews:wine_detail', args=(wine.id,)))    # 重定向

    return render(request, 'reviews/wine_detail.html', {'wine': wine, 'form': form})



def user_review_list(request, username=None):
    if not username:
        username = request.user.username
    latest_review_list = Review.objects.filter(user_name=username).order_by('-pub_date')
    context = {'latest_review_list':latest_review_list, 'username':username}
    return render(request, 'reviews/user_review_list.html', context)