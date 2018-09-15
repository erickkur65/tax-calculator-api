# Generated by Django 2.0.7 on 2018-09-15 04:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bill', '0002_bill_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='billitem',
            name='qty',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='billitem',
            name='tax_amount',
            field=models.DecimalField(decimal_places=4, max_digits=16, null=True),
        ),
        migrations.AddField(
            model_name='billitem',
            name='total_amount',
            field=models.DecimalField(decimal_places=4, max_digits=16, null=True),
        ),
    ]