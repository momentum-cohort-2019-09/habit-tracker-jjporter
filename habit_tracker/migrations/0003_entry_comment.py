# Generated by Django 2.2.7 on 2019-11-12 00:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('habit_tracker', '0002_habit_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='comment',
            field=models.TextField(default='', max_length=255),
            preserve_default=False,
        ),
    ]
