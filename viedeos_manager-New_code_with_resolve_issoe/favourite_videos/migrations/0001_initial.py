# Generated by Django 3.0.7 on 2020-08-06 09:40

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account', '0001_initial'),
        ('videos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='VsSendEmailForNewVideo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Send_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('Videos', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='VsVideos_SendEmailForNewVideo', to='videos.VsVideos')),
                ('VsUser', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='User_SendEmailForNewVideo', to='account.VsUsers')),
            ],
            options={
                'verbose_name_plural': 'VS Send Email For New Video Upload.',
            },
        ),
        migrations.CreateModel(
            name='VsFavourite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Create_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('Subscribe', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='VsUsers_VsFavourite', to='account.VsUsers')),
                ('Video', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='VideoFavourite', to='videos.VsVideos')),
                ('VsUser', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='User_VsFavourite', to='account.VsUsers')),
            ],
            options={
                'verbose_name_plural': 'VS Favourite',
            },
        ),
    ]