from django.urls import include, path, re_path 
from rest_framework.urlpatterns import format_suffix_patterns

from . import views 

urlpatterns = [
    path('api/v1/hospitals/', views.HospitalName.as_view()),
    path('api/v1/hospitals/<int:id>/', views.HospitalAdd.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)
