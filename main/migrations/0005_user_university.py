# Generated by Django 4.2.6 on 2024-05-30 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_user_groups_user_user_permissions'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='university',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
