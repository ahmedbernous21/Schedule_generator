# Generated by Django 4.2.6 on 2024-06-24 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0022_remove_schedule_grade_remove_schedule_school_year_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='name',
            field=models.CharField(blank=True, null=True),
        ),
    ]
