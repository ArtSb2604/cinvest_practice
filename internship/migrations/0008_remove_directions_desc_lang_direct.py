# Generated by Django 4.1.7 on 2023-04-08 15:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('internship', '0007_directions_data_menu_directionsdesc_data_menu'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='directions',
            name='desc_lang_direct',
        ),
    ]
