# Generated by Django 4.0.3 on 2022-04-10 20:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_picture_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='picture',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to='site_media/', verbose_name='Картинка'),
        ),
    ]
