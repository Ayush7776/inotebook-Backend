# Generated by Django 5.0.4 on 2024-11-07 11:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_rename_profile_pic_user_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='image',
            new_name='profile_pic',
        ),
    ]