from django.http import HttpResponse
from django.shortcuts import redirect
from django.views import generic
from django.views.generic import DetailView
from rest_framework import generics
from rest_framework.authentication import SessionAuthentication, BasicAuthentication

from users.forms import UserInfo
from users.models import User
from users.serilazer import UserSerializer


class UserAdminListView(generic.ListView):
    model = User
    context_object_name = 'users'
    template_name = 'users/admin-user.html'


class CsrfExemptSessionAuthentication(SessionAuthentication):
    def enforce_csrf(self, request):
        return


class UserAPIList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)


def user_update_status(request):
    if request.method == 'GET':
        user = User.objects.get(pk=request.GET['user_id'])
        user.Activity = bool(int(request.GET['status']))
        user.save()
        if bool(int(request.GET['status'])):
            return HttpResponse(
                f'<button type="button" class="btn btn-dark button-admin-1" id="user_status{request.GET["user_id"]}" onclick="status_user({request.GET["user_id"]});" href="#" data-userid="{request.GET["user_id"]}" data-status="0">Заблокировать</button>')
        else:
            return HttpResponse(
                f'<button type="button" class="btn btn-dark button-admin-4" id="user_status{request.GET["user_id"]}" onclick="status_user({request.GET["user_id"]});" href="#" data-userid="{request.GET["user_id"]}" data-status="1">Активировать</button>')

    else:
        return HttpResponse("Request method is not a GET")


def user_delete(request):
    if request.method == 'GET':
        User.objects.get(pk=request.GET['user_id']).delete()
        return HttpResponse("Success!")  # Sending an success response
    else:
        return HttpResponse("Request method is not a GET")


class UserDetail(DetailView):
    model = User
    form_class = UserInfo
    template_name = "users/user_detail.html"
    context_object_name = 'user'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = UserInfo
        return context

    def post(self, request, *args, **kwargs):
        form = request.POST
        print(form)
        User.objects.filter(pk=form['user_pk']).update(last_name=form['last_name'], first_name=form['first_name'],
                                                       mail=form['mail'], email=form['mail'],
                                                       patronymic=form['patronymic'], birthdate=form['birthdate'],
                                                       city=form['city'], number_phone=form['number_phone'],
                                                       social_contact=form['social_contact'],
                                                       course=form['course'], university=form['university'],
                                                       department=form['department'],
                                                       specialization=form['specialization'],
                                                       year_graduation=form['year_graduation'],
                                                       average_score=form['average_score'],
                                                       educational_interests=form['educational_interests'],
                                                       what_tasks=form['what_tasks'], achievements=form['achievements'],
                                                       work_experience=form['work_experience'],
                                                       find_out=form['find_out'],
                                                       interested_internship=form['interested_internship'])
        return redirect('all_users')
