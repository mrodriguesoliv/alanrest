# Generated by Django 5.1.2 on 2024-10-28 23:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0017_conversation_unique_conversation_per_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reminder',
            name='user',
        ),
    ]