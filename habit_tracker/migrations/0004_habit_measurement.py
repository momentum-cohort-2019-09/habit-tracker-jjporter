# Generated by Django 2.2.7 on 2019-11-12 02:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('habit_tracker', '0003_entry_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='habit',
            name='measurement',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
    ]