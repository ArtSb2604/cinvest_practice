from django.views import generic

from internship.models import Directions


class HomeListView(generic.ListView):
    model = Directions
    context_object_name = 'Cards'
    template_name = 'internship/index.html'
