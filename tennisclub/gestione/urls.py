"""
URL configuration for tennisclub project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from .views import *

app_name = 'gestione'

urlpatterns = [
    path('', home, name='home'),
    path('player_list/', player_list, name='player_list'),
    path('add_player/', add_player, name='add_player'),
    path('player_list_class/', PlayerListView.as_view(), name='player_list_class'),
    path('add_player_class/', PlayerCreateView.as_view(), name='add_player_class'),
    path('detail/<pk>/', PlayerDetailView.as_view(), name='player_detail'),
    path('update/<pk>/', PlayerUpdateView.as_view(), name='player_update'),
    path('delete/<pk>/', PlayerDeleteView.as_view(), name='player_delete'),
    path("search/", search, name="search"),
    path("searchresults/<str:sstring>/<str:where>/", SearchResultsList.as_view(), name="searchresults")
]
