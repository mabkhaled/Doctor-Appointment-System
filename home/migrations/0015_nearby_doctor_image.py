# Generated by Django 4.1 on 2022-11-26 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0014_nearby_doctor_frday_ev_nearby_doctor_frday_mor_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='nearby_doctor',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
