# Generated by Django 3.2.8 on 2021-10-25 17:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0006_alter_book_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='id',
            new_name='google_book_id',
        ),
    ]
