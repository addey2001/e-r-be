from django.urls import path
from elevate.views import ElevateView, ElevateDetailView


urlpatterns = [
    path('', ElevateView.as_view()),
    path('<int:pk>/', ElevateDetailView.as_view())
]