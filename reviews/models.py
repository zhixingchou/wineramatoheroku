# coding: utf-8
# 添加中文注释要使用utf-8编码
from django.db import models
import numpy as np


class Wine(models.Model):
    name = models.CharField(max_length=200)
    
    def average_rating(self):
	# map(function, sequence) ：对sequence中的item依次执行function(item)，见执行结果组成一个List返回
	# lambda lambda其实就是一条语句，lambda(x):body。x是lambda函数的参数，参数可以有任意多个(包括可选参数);body是函数体，只能是一个表达式，并且直接返回该表达式的值
	# 对于用`` ForeignKey`` 来定义的关系来说，在关系的另一端也能反向的追溯回来【self.review_set.all()】
        all_ratings = map(lambda x: x.rating, self.review_set.all())
	# 求list平均值与average有区别
	# https://stackoverflow.com/questions/20054243/np-mean-vs-np-average-in-python-numpy
        return np.mean(all_ratings)
        
    def __unicode__(self):
        return self.name


class Review(models.Model):
    RATING_CHOICES = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    )
    wine = models.ForeignKey(Wine)
    pub_date = models.DateTimeField('date published')
    user_name = models.CharField(max_length=100)
    comment = models.CharField(max_length=200)
    rating = models.IntegerField(choices=RATING_CHOICES)
    
