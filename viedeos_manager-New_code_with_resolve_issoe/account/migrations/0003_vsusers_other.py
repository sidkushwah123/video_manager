# Generated by Django 3.0.7 on 2020-08-12 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_auto_20200808_0946'),
    ]

    operations = [
        migrations.AddField(
            model_name='vsusers',
            name='Other',
            field=models.CharField(blank=True, default='Coach', max_length=120, null=True),
        ),
    ]
