# Generated by Django 5.0.7 on 2024-07-23 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courseCompassApp', '0002_remove_user_aimessage_remove_user_usermessage_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='messages',
            field=models.JSONField(blank=True, default=list),
        ),
    ]