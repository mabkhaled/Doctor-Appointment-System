# Generated by Django 4.1.3 on 2022-12-11 04:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_alter_review_time'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='review',
            new_name='reviewers',
        ),
    ]
