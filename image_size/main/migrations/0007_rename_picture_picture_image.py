# Generated by Django 4.0.3 on 2022-04-10 21:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_alter_picture_picture'),
    ]

    operations = [
        migrations.RenameField(
            model_name='picture',
            old_name='picture',
            new_name='image',
        ),
    ]
