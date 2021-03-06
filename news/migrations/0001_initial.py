# Generated by Django 3.2.dev20201223162125 on 2021-01-08 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('article_title', models.CharField(max_length=150, verbose_name='Title')),
                ('announcement', models.CharField(max_length=250, verbose_name='Announcement')),
                ('article_content', models.TextField(verbose_name='Article content')),
                ('pub_date', models.DateTimeField(default='2021-01-08 11:50:59', verbose_name='Publication date')),
            ],
            options={
                'verbose_name': 'Article',
                'verbose_name_plural': 'Articles',
            },
        ),
    ]
