# Generated by Django 2.0.4 on 2018-04-22 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_post', '0002_blogpostmodel_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpostmodel',
            name='created_time',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='blogpostmodel',
            name='updated_time',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
