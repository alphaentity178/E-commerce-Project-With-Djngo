# Generated by Django 5.0.6 on 2024-09-09 11:34

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_Order', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ordered', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('paymentId', models.CharField(blank=True, max_length=264, null=True)),
                ('orderId', models.CharField(blank=True, max_length=200, null=True)),
                ('orderitems', models.ManyToManyField(to='App_Order.cart')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='Orer',
        ),
    ]