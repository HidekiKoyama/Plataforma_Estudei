# Generated by Django 4.2.2 on 2023-07-09 01:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sistema', '0023_rename_friens_friends'),
    ]

    operations = [
        migrations.RenameField(
            model_name='courses',
            old_name='categorie_couse',
            new_name='categorie_course',
        ),
    ]
