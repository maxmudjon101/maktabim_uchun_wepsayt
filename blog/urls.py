from django.urls import path
from .views import home,about,aloqa





urlpatterns = [
    path('',home,name='saxifa'),
    path('aloqa/',aloqa,name='alo'),
    path('about/',about,name='haqida'),
]



