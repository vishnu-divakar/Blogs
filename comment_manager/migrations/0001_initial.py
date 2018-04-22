# Generated by Django 2.0.4 on 2018-04-22 10:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('blog_post', '0003_auto_20180422_1530'),
    ]

    operations = [
        migrations.CreateModel(
            name='CommentManager',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=25, null=True)),
                ('comment', models.TextField()),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('updated_time', models.DateTimeField(auto_now=True)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog_post.BlogPostModel')),
            ],
        ),
    ]
