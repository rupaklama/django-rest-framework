# Generated by Django 3.0.7 on 2020-06-15 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_customer_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='email',
            field=models.EmailField(max_length=254, null=True, unique=True),
        ),
    ]
