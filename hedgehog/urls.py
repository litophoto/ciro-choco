from django import path

from . import views

app_name = 'hedgehog'
urlpatterns = [
    path('', views.Index.as_view(), name='index'),
]