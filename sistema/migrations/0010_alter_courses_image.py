# Generated by Django 4.2.1 on 2023-07-02 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sistema', '0009_courses_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courses',
            name='image',
            field=models.ImageField(default='', upload_to=None),
        ),
    ]
