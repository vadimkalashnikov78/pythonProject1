# Generated by Django 4.1.7 on 2024-02-12 08:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0009_wish_delete_wishlist'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='wish',
            name='product',
        ),
    ]
