# Generated by Django 4.1.6 on 2023-03-21 17:23

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_remove_comment_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='intro',
            field=ckeditor.fields.RichTextField(max_length=500),
        ),
    ]
