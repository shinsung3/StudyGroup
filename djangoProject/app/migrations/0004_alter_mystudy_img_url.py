# Generated by Django 3.2.3 on 2021-06-05 03:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_mystudy_board_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mystudy',
            name='img_url',
            field=models.FileField(null=True, upload_to=''),
        ),
    ]