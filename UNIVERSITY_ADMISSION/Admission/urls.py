from django.urls import path
from .views import MajorList

urlpatterns = [
    path('MajorList', MajorList.as_view()),
   
]
