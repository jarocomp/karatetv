# Generated by Django 5.0.7 on 2024-11-06 19:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('karatetv', '0003_rename_post_postse_posttv'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='postse',
            options={'ordering': ['created_date']},
        ),
        migrations.AlterModelOptions(
            name='posttv',
            options={'ordering': ['created_date']},
        ),
    ]