# Generated by Django 2.0.7 on 2018-09-15 01:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TaxItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=64)),
                ('tax_code', models.SmallIntegerField()),
                ('tax_type', models.CharField(max_length=20)),
                ('amount', models.DecimalField(decimal_places=4, max_digits=16)),
                ('tax_amount', models.DecimalField(decimal_places=4, max_digits=16)),
                ('total_amount', models.DecimalField(decimal_places=4, max_digits=16)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
