# Generated by Django 4.1.7 on 2023-04-09 03:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_remove_user_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='categories',
            field=models.CharField(default=1, max_length=100, verbose_name='Направление'),
            preserve_default=False,
        ),
    ]