# Generated by Django 3.2.5 on 2021-07-21 06:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='banner',
            options={'verbose_name_plural': '1. Banners'},
        ),
        migrations.AlterModelOptions(
            name='brand',
            options={'verbose_name_plural': '3. Brands'},
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': '2. Categories'},
        ),
        migrations.AlterModelOptions(
            name='color',
            options={'verbose_name_plural': '4. Colors'},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name_plural': '6. Products'},
        ),
        migrations.AlterModelOptions(
            name='productattribute',
            options={'verbose_name_plural': '7. ProductAttributes'},
        ),
        migrations.AlterModelOptions(
            name='size',
            options={'verbose_name_plural': '5. Sizes'},
        ),
    ]