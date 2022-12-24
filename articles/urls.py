from django.urls import path
from django.contrib import admin
from . import views

app_name = 'articles'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name ='home'),
    path('<slug>/', views.article_detail, name='detail')
]
