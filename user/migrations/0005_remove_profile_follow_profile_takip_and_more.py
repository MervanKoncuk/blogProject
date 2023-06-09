# Generated by Django 4.1.3 on 2023-03-21 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_alter_profile_follow_alter_profile_followers'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='follow',
        ),
        migrations.AddField(
            model_name='profile',
            name='takip',
            field=models.ManyToManyField(blank=True, to='user.profile', verbose_name='Takip'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='followers',
            field=models.ManyToManyField(blank=True, to='user.profile', verbose_name='Takipçiler'),
        ),
    ]
