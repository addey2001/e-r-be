from django.urls import path
from elevate.views import ElevateView, ElevateDetailView, ListingFavoriteView


urlpatterns = [
    path('', ElevateView.as_view()),
    path('<int:pk>/', ElevateDetailView.as_view()),
    path('<int:pk>/favorites/', ListingFavoriteView.as_view()),
]