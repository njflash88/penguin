# Generated by Django 4.2 on 2024-09-23 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emaillists', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emaillist',
            name='email',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='emaillist',
            name='name',
            field=models.CharField(max_length=255),
        ),
    ]
