from django.urls import path

from users import views
from users.views import UserAdminListView, UserDetail, UserAPIList, ApplicationsAdminListView, LoginView, AdminView

urlpatterns = [
    path('', AdminView.as_view(), name="AdminView"),
    path('users/', UserAdminListView.as_view(), name="all_users"),
    path("users/user_update_status", views.user_update_status, name="user_update_status"),
    path("users/delete_user", views.user_delete, name="delete_user"),
    path("users/<int:pk>/", UserDetail.as_view(), name="user_detail"),
    path('applications/', ApplicationsAdminListView.as_view(), name="all_applications"),
]