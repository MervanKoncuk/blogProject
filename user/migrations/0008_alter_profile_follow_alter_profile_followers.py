# Generated by Django 4.1.3 on 2023-03-21 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0007_profile_follow_alter_profile_followers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='follow',
            field=models.ManyToManyField(blank=True, related_name='takip', to='user.profile', verbose_name='Takip'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='followers',
            field=models.ManyToManyField(blank=True, related_name='takipci', to='user.profile', verbose_name='Takipçiler'),
        ),
    ]