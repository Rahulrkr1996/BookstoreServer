# Generated by Django 3.2.8 on 2021-10-24 20:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0002_alter_book_author'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='img',
            new_name='image',
        ),
    ]