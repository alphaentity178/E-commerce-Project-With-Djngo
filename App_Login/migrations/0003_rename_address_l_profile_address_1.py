# Generated by Django 4.2.16 on 2024-09-12 18:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App_Login', '0002_alter_user_is_active'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='address_l',
            new_name='address_1',
        ),
    ]
