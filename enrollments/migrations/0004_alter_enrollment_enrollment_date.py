# Generated by Django 4.2 on 2024-09-30 01:15

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('enrollments', '0003_alter_enrollment_student'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enrollment',
            name='enrollment_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
