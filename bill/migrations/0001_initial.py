# Generated by Django 3.2 on 2021-04-25 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('generated_on', models.DateTimeField(auto_now_add=True)),
                ('customer_name', models.CharField(max_length=200)),
                ('total_units_consumed', models.IntegerField(verbose_name='Units of electricity consumed')),
                ('amount_payable', models.FloatField(verbose_name='Due Amount')),
                ('image_of_meter', models.ImageField(upload_to='images/')),
            ],
        ),
    ]