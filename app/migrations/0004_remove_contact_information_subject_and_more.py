# Generated by Django 5.0.4 on 2024-04-21 22:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_contact_information'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact_information',
            name='subject',
        ),
        migrations.RemoveField(
            model_name='contact_information',
            name='timestamp',
        ),
        migrations.AlterField(
            model_name='contact_information',
            name='email',
            field=models.EmailField(help_text='Please enter a valid email address', max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='contact_information',
            name='message',
            field=models.TextField(null=True),
        ),
    ]
