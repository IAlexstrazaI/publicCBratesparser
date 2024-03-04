from django.urls import path
from . import views

from django.urls import path

from article.views import ArticleDetailView


urlpatterns = [
 path('', views.index, name='index'),
 path('cities/', views.CitiesListView.as_view(), name='cities'),
 path('city_detail/<int:tcode>', views.CityDetailView.as_view(), name='city-detail'),
 path("<slug:slug>/", ArticleDetailView.as_view(), name="article-detail"),
]