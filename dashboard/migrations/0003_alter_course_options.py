# Generated by Django 5.0.6 on 2024-08-20 22:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_course_days_course_end_time_course_room_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='course',
            options={'permissions': [('change_about', 'Can change the about course'), ('change_syllabus', 'Can change the syllabus of the course')]},
        ),
    ]
