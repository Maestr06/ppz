# Generated by Django 3.2.12 on 2022-09-19 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_alter_product_img_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='img_url',
            field=models.URLField(default='https://auto-club.hyundai.pl/fileadmin/_processed_/d/3/csm_i30_hb_nline_dummy_02_5x4_ef82ba5a5c.png'),
        ),
    ]
