# Generated by Django 5.0.6 on 2024-08-12 22:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_web', '0002_alter_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(upload_to='img/kits/'),
        ),
    ]
