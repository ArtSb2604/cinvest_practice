from django.views import generic
from users.models import User


class UserAdminListView(generic.ListView):
    model = User
    context_object_name = 'Cards'
    template_name = 'users/admin-user.html'
