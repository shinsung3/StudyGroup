# Generated by Django 3.2.3 on 2021-06-02 16:30

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='mystudy',
            name='board_text',
            field=ckeditor.fields.RichTextField(null=True),
        ),
    ]
