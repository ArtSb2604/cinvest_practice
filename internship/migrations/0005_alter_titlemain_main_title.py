# Generated by Django 4.1.7 on 2023-04-08 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('internship', '0004_directionsdesc_titlemain_remove_directions_city_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='titlemain',
            name='main_title',
            field=models.TextField(verbose_name='div'),
        ),
    ]
