# Generated by Django 3.2.8 on 2021-10-25 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0005_alter_book_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='id',
            field=models.CharField(max_length=20, primary_key=True, serialize=False),
        ),
    ]
