# Generated by Django 4.2.2 on 2023-06-16 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_remove_subtask_task_subtask_parent_task_task_subtask_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='category',
            field=models.CharField(max_length=100),
        ),
    ]
