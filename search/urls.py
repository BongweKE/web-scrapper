# search/urls.py
from django.urls import path,include

from . import views 



urlpatterns = [
    path('history', views.HistoryView, name='history'),
    path('', views.SearchView, name='search'),
]


