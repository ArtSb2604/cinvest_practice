from django.views import generic

from internship.models import Directions, TitleMain, DirectionsDesc


class HomeListView(generic.ListView):
    model = TitleMain
    context_object_name = 'TitleMain'
    template_name = 'internship/index.html'

    def get_context_data(self, **kwargs):
        context = super(HomeListView, self).get_context_data(**kwargs)
        context['Directions'] = Directions.objects.all()
        context['DirectionsDesc'] = DirectionsDesc.objects.all()
        return context
