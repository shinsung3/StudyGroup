# Generated by Django 3.2.3 on 2021-06-05 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_auto_20210605_2214'),
    ]

    operations = [
        migrations.AddField(
            model_name='mystudy',
            name='is_finish',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
