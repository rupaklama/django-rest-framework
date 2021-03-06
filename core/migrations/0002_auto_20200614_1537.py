# Generated by Django 3.0.7 on 2020-06-14 15:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DataSheet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=50)),
                ('historical_data', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Profession',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='customer',
            name='document',
        ),
        migrations.AddField(
            model_name='document',
            name='customer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.Customer'),
        ),
        migrations.AlterField(
            model_name='document',
            name='document_type',
            field=models.CharField(choices=[('PP', 'Passport'), ('ID', 'Identity card'), ('OT', 'Others')], max_length=2),
        ),
        migrations.AddField(
            model_name='customer',
            name='data_sheet',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.DataSheet'),
        ),
        migrations.AddField(
            model_name='customer',
            name='professions',
            field=models.ManyToManyField(to='core.Profession'),
        ),
    ]
