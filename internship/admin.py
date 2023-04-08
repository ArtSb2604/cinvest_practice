from django.contrib import admin

from internship.models import Directions, DirectionsDesc, TitleMain
from django.contrib.auth.models import Group

admin.site.unregister(Group)
admin.site.register(Directions)
admin.site.register(DirectionsDesc)
admin.site.register(TitleMain)

admin.site.site_header = 'HR Администрация'
admin.site.site_title = 'Стажировка в Банк Центр-инвест'
