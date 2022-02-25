# Generated by Django 3.2.10 on 2022-02-25 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_order_reff'),
    ]

    operations = [
        migrations.CreateModel(
            name='Shipping',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reff', models.SlugField(max_length=255)),
                ('services', models.CharField(max_length=255)),
                ('receipt_number', models.CharField(max_length=255)),
                ('receipt_img', models.FileField(upload_to='ship/')),
            ],
        ),
    ]
