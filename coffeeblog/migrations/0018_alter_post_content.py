# Generated by Django 3.2.13 on 2022-05-23 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coffeeblog', '0017_alter_post_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.TextField(blank=True, null=True),
        ),
    ]
