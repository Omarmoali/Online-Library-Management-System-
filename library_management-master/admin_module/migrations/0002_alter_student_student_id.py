# Generated by Django 5.1.1 on 2024-10-12 03:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_module', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='student_id',
            field=models.IntegerField(max_length=10, unique=True),
        ),
    ]
