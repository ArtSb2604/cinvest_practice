from django.urls import path
from internship.views import HomeListView

urlpatterns = [
    path('', HomeListView.as_view()),
]