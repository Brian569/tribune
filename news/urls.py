from django.urls import path
from django.urls.conf import re_path
from .views import (
    welcome,
    news_of_day,past_days_news

)

urlpatterns = [
    path('', welcome, name='welcome'),
    path('today', news_of_day, name='newsToday'),
    re_path(r'archives/(\d{4}-\d{2}-\d{2})', past_days_news , name='pastNews')
]