# Generated by Django 4.1 on 2022-11-22 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_remove_nearby_doctor_brife_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='nearby_doctor',
            name='brife',
            field=models.TextField(default=' '),
            preserve_default=False,
        ),
    ]
