from django.urls import re_path
from .views import  DataSet

urlpatterns = [
    re_path(r'^dataset/search/$', DataSet.as_view()),
]
