# Generated by Django 4.1.3 on 2022-12-02 07:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tamueats', '0006_remove_customer_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='foodproductcategory',
            name='featured_product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='tamueats.foodproduct'),
        ),
    ]
