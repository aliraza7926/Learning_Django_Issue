from django.urls import path
from .views import IssuView
urlpatterns =[
    path('',IssuView.as_view(), name='home')
]