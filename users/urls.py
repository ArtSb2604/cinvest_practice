from django.urls import path
from users.views import UserAdminListView

urlpatterns = [
    path('', UserAdminListView.as_view()),
]
