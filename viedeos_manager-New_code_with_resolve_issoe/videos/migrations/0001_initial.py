# Generated by Django 3.0.7 on 2020-08-06 09:40

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import videos.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account', '0001_initial'),
        ('categorys_and_reatings', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='VsVideos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Videos_Title', models.CharField(max_length=500)),
                ('Videos_id', models.CharField(max_length=500)),
                ('Videos_Slug', models.CharField(blank=True, max_length=500, null=True)),
                ('Video', models.FileField(null=True, upload_to=videos.models.user_directory_path)),
                ('Video_thumbnail', models.ImageField(blank=True, null=True, upload_to=videos.models.user_directory_path_thumbnail)),
                ('Publich_Status', models.BooleanField(default=False)),
                ('Country', models.CharField(blank=True, max_length=120, null=True)),
                ('Description', models.TextField(blank=True, null=True)),
                ('Meta_Title', models.CharField(blank=True, max_length=200, null=True)),
                ('Meta_keyword', models.CharField(blank=True, max_length=120, null=True)),
                ('Meta_description', models.TextField(blank=True, null=True)),
                ('Created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('Views', models.IntegerField(default=0)),
                ('Reating', models.IntegerField(default=0)),
                ('Updated_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('mail_send_status', models.BooleanField(default=False)),
                ('Categoryes', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='VsCategory_VsVideos', to='categorys_and_reatings.VsCategory')),
                ('Created_By', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='User_VsVideos', to='account.VsUsers')),
                ('Sub_Categoryes', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='VsSubCategoryes_VsVideos', to='categorys_and_reatings.VsSubCategoryes')),
            ],
            options={
                'verbose_name_plural': 'VS Videos',
            },
        ),
        migrations.CreateModel(
            name='VsRating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Reating', models.IntegerField(default=0)),
                ('Status', models.BooleanField(default=True)),
                ('Created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('Updated_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('Reating_attrbute', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='User_VsReatingAttribute', to='categorys_and_reatings.VsReatingAttribute')),
                ('User', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='VsUsers_VsReating', to='account.VsUsers')),
                ('Video', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='VsVideos_VsReating', to='videos.VsVideos')),
            ],
            options={
                'verbose_name_plural': 'VS Rating',
            },
        ),
        migrations.CreateModel(
            name='VsNonRegisterUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=500, null=True)),
                ('watch_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('User_ip', models.CharField(blank=True, max_length=500, null=True)),
                ('Video', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='VsVideos_VsNonRegisterUser', to='videos.VsVideos')),
            ],
            options={
                'verbose_name_plural': 'VS Non Register User',
            },
        ),
        migrations.CreateModel(
            name='VsComments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Comment', models.TextField()),
                ('Status', models.BooleanField(default=True)),
                ('Created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('Updated_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('User', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='User_VsComments', to='account.VsUsers')),
                ('Video', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='User_VsComments', to='videos.VsVideos')),
            ],
            options={
                'verbose_name_plural': 'VS Comments',
            },
        ),
    ]
