# coding: utf-8
from django.forms import ModelForm, Textarea
from reviews.models import Review


class ReviewForm(ModelForm):
    # 表单的内部类 Meta
    class Meta:
        model = Review
        fields = ['rating', 'comment']     # 表单显示字段
        widgets = {
            'comment': Textarea(attrs={'cols': 40, 'rows': 15}),    # 重写字段的控件属性
        }