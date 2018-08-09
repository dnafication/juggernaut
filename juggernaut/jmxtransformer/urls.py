from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('jmxdetails/<int:jmx_id>/', views.details, name='details')
]