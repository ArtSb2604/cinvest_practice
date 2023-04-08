from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from users import views
from users.views import UserAPIList, LoginView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('internship.urls')),
    path('chat/', include('chat.urls')),
    path('moderator/', include('users.urls')),
    path("api/v1/users/create/", UserAPIList.as_view(), name="user_create"),
    path('summernote/', include('django_summernote.urls')),
    path('practicum/', include('practicum.urls')),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', views.logout_view, name='logout'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_URL)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
