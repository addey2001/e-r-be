from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView
from .views import SignupView


urlpatterns = [
    path('sign-up/', SignupView.as_view()),
    path('sign-in/', TokenObtainPairView.as_view())

]