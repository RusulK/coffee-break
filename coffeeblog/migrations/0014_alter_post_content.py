# Generated by Django 3.2.13 on 2022-05-20 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coffeeblog', '0013_post_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.TextField(),
        ),
    ]
