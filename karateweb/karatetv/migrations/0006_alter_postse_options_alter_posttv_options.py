# Generated by Django 5.0.7 on 2024-11-06 19:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('karatetv', '0005_alter_postse_options_alter_posttv_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='postse',
            options={'ordering': ['-published_date']},
        ),
        migrations.AlterModelOptions(
            name='posttv',
            options={'ordering': ['-published_date']},
        ),
    ]
