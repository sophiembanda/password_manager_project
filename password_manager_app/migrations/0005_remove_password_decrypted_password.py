# Generated by Django 5.0.3 on 2024-04-02 11:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('password_manager_app', '0004_alter_password_encrypted_password'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='password',
            name='decrypted_password',
        ),
    ]
