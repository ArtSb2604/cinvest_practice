from django.contrib import admin

from internship.models import Directions

admin.site.register(Directions)

admin.site.site_header = 'HR Администрация'
admin.site.site_title = 'Стажировка в Банк Центр-инвест'
