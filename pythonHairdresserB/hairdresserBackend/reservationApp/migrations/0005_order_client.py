# Generated by Django 4.0 on 2024-05-17 00:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reservationApp', '0004_remove_session_name_remove_session_surname'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='client',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='reservationApp.client'),
        ),
    ]
