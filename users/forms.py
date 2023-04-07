from django import forms


class UserInfo(forms.Form):
    surname = forms.CharField(label='Фамилия', max_length=100)
    name = forms.CharField(label='Имя', max_length=100)
    patronymic = forms.CharField(label='Отчество', max_length=100)
    birthdate = forms.DateField(label='Дата рождения', max_length=100)
    city = forms.CharField(label='Город', max_length=100)
    number_phone = forms.CharField(label='Телефон', max_length=100)
    mail = forms.CharField(label='Электронная почта', max_length=100)
    social_contact = forms.CharField(label='Контакт для оперативной связи (Телеграм, VK или что-то ещё)', max_length=100)
    course = forms.CharField(label='Укажите вашу ступень обучения', max_length=100)
    university = forms.CharField(label='Расскажите, какого университета', max_length=100)
    department = forms.CharField(label='Кафедра', max_length=100)
    specialization = forms.CharField(label='Специальность', max_length=100)
    year_graduation = forms.CharField(label='Укажите год окончания', max_length=100)
    average_score = forms.CharField(label='Укажите ваш средний балл в вузе', max_length=100)
    educational_interests = forms.CharField(label='Расскажите о своих учебных интересах:', max_length=100)
    what_tasks = forms.CharField(label='Опишите, какими задачами вам было бы интересно заниматься во время стажировки', max_length=100)
    achievements = forms.CharField(label='Расскажите о своих достижениях', max_length=100)
    work_experience = forms.CharField(label='Если у вас есть опыт работы/стажировки, расскажите об этом подробнее', max_length=100)
    find_out = forms.CharField(label='Откуда вы узнали о стажировках в Банке Центр-Инвест', max_length=100)
    interested_internship = forms.CharField(label='Почему вас заинтересовала стажировка в Банке Центр-Инвест, и чего вы от неё ждёте?', max_length=100)
    resume = forms.FileField(label='Добавьте резюме')

