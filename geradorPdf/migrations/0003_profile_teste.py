# Generated by Django 3.1.7 on 2021-03-08 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geradorPdf', '0002_remove_profile_skills'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='teste',
            field=models.CharField(default='ee', max_length=20, verbose_name='teste'),
            preserve_default=False,
        ),
    ]
