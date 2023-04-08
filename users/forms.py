from django import forms


class UserInfo(forms.Form):
    last_name = forms.CharField(label='Фамилия', max_length=100, required=False)
    name = forms.CharField(label='Имя', max_length=100, required=False)
    patronymic = forms.CharField(label='Отчество', max_length=100, required=False)
    birthdate = forms.DateField(label='Дата рождения')
    city = forms.CharField(label='Город', max_length=100, required=False)
    number_phone = forms.CharField(label='Телефон', max_length=100, required=False)
    mail = forms.CharField(label='Электронная почта', max_length=100, required=False)
    social_contact = forms.CharField(label='Контакт для оперативной связи (Телеграм, VK или что-то ещё)', max_length=100, required=False)
    course = forms.CharField(label='Укажите вашу ступень обучения', max_length=100)
    university = forms.CharField(label='Расскажите, какого университета', max_length=100)
    department = forms.CharField(label='Кафедра', max_length=100, required=False)
    specialization = forms.CharField(label='Специальность', max_length=100, required=False)
    year_graduation = forms.CharField(label='Укажите год окончания', max_length=100, required=False)
    average_score = forms.CharField(label='Укажите ваш средний балл в вузе', max_length=100, required=False)
    educational_interests = forms.CharField(label='Расскажите о своих учебных интересах:', max_length=100, required=False)
    what_tasks = forms.CharField(label='Опишите, какими задачами вам было бы интересно заниматься во время стажировки', max_length=100, required=False)
    achievements = forms.CharField(label='Расскажите о своих достижениях', max_length=100, required=False)
    work_experience = forms.CharField(label='Если у вас есть опыт работы/стажировки, расскажите об этом подробнее', max_length=100, required=False)
    find_out = forms.CharField(label='Откуда вы узнали о стажировках в Банке Центр-Инвест', max_length=100, required=False)
    interested_internship = forms.CharField(label='Почему вас заинтересовала стажировка в Банке Центр-Инвест, и чего вы от неё ждёте?', max_length=100, required=False)
    resume = forms.FileField(label='Добавьте резюме', required=False)

    def __init__(self, *args, **kwargs):
        super(UserInfo, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'user-input'

