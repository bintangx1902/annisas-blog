# Generated by Django 3.2.7 on 2021-10-13 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0013_productreview_p_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productreview',
            name='p_img',
            field=models.CharField(default='', max_length=255, verbose_name='Link Gambar Produk'),
        ),
    ]