# Generated by Django 4.1.3 on 2023-03-21 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_remove_profile_takip_alter_profile_followers'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='follow',
            field=models.ManyToManyField(blank=True, to='user.profile', verbose_name='Takip'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='followers',
            field=models.ManyToManyField(blank=True, to='user.profile', verbose_name='Takipçiler'),
        ),
    ]
