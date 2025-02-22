# Generated by Django 5.1.6 on 2025-02-17 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_alter_student_contract_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='sponsor',
            name='custom_amount',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='sponsor',
            name='amount',
            field=models.CharField(choices=[('1_000_000', '1 MLN UZS'), ('5_000_000', '5 MLN UZS'), ('7_000_000', '7 MLN UZS'), ('10_000_000', '10 MLN UZS'), ('30_000_000', '30 MLN UZS'), ('OTHER', 'OTHERS')], max_length=30),
        ),
        migrations.AlterField(
            model_name='sponsor',
            name='sponsor_status',
            field=models.CharField(choices=[('YURIDIK SHAXS', 'Yuridik shaxs'), ('JISMONIY SHAXS', 'Jismoniy shaxs')], max_length=50),
        ),
    ]
