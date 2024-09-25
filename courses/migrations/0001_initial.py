# Generated by Django 4.2 on 2024-09-24 15:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('instructors', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('catagory', models.CharField(max_length=20)),
                ('keyword', models.CharField(max_length=50)),
                ('price', models.IntegerField()),
                ('prerequisite', models.CharField(max_length=10)),
                ('deadline', models.DateField()),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('max_enrollment', models.BigIntegerField()),
                ('location', models.CharField(max_length=15)),
                ('instructor_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='instructors.instructor')),
            ],
        ),
    ]
