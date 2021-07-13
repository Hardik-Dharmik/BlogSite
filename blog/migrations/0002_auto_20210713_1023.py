# Generated by Django 3.2.4 on 2021-07-13 04:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='user',
        ),
        migrations.AddField(
            model_name='post',
            name='author',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
    ]