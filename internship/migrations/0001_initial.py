# Generated by Django 3.1.14 on 2023-04-07 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Directions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('directions_name', models.CharField(max_length=200, verbose_name='Название направления')),
                ('desc_lang_direct', models.CharField(max_length=200, verbose_name='Описание языков направления')),
                ('city', models.CharField(max_length=200, verbose_name='Город')),
                ('what_to_do', models.EmailField(max_length=200, verbose_name='Чем занимаются')),
                ('desc_wtd', models.TextField(max_length=1000, verbose_name='Описание направления')),
            ],
            options={
                'verbose_name': 'Направление',
                'verbose_name_plural': 'Направления',
            },
        ),
    ]
