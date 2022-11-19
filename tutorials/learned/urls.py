from django.urls import path
from . import views

app_name='learned'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index' ),
    path('<int:pk>/', views.ContentDetailView.as_view(), name='detail'),
    path('search/', views.search, name='search'),
    path('all/', views.all, name='all'),

]
