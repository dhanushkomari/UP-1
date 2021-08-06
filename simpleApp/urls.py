from django.urls import path
from . import views

app_name = 'simpleApp'

urlpatterns = [
    # path('', views.form),
    path('test', views.test)
]
