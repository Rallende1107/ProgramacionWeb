from django.urls import path
from .  import views

urlpatterns = [
    path('home2/', views.IndexDosView.as_view()),
]
