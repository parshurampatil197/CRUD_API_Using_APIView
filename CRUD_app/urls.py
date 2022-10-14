from django.urls import path
from .views import StudentView

urlpatterns = [
    path('crud/', StudentView.as_view()),
    path('crud/<int:id>/', StudentView.as_view()),
]
