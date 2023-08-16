from django.urls import path

from .views import FilteredMajorList, MajorList

urlpatterns = [
    path('MajorList', MajorList.as_view()),
    path('filtered-major-list', FilteredMajorList.as_view()),
   
]
