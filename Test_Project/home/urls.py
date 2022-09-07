from django.urls import path
from . import views
# from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('home/', views.TestApiView.as_view(), name = 'Test'),
    path('home/<str:pk>/', views.TestApiView.as_view(), name = 'TestDetail'),
]


# urlpatterns = format_suffix_patterns(urlpatterns)
