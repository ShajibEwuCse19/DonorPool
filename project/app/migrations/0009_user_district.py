# Generated by Django 4.0.5 on 2022-08-26 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_user_age'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='district',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]