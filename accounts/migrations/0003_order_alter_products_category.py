# Generated by Django 5.0.4 on 2024-04-10 03:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_products'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Out for Delivery', 'Out for Delivery'), ('Delivered', 'Delivered')], max_length=200, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='products',
            name='category',
            field=models.CharField(choices=[('Indoor', 'Indoor'), ('Outdoor', 'Outdoor')], max_length=200, null=True),
        ),
    ]