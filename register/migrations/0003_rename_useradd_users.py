# Generated by Django 4.1.6 on 2023-04-02 10:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("register", "0002_alter_useradd_first_name_alter_useradd_last_name"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Useradd",
            new_name="Users",
        ),
    ]
