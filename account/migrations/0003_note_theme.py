# Generated by Django 5.0.4 on 2024-10-30 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_note'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='theme',
            field=models.TextField(default='light'),
        ),
    ]