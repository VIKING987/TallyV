# Generated by Django 4.0 on 2022-01-11 19:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(blank=True, default=None)),
                ('disp_thru', models.CharField(blank=True, default=None, max_length=20, verbose_name='Dispatched Through')),
                ('bales', models.CharField(blank=True, default=None, max_length=20)),
                ('delivery', models.CharField(blank=True, default=None, max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Party',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, verbose_name='Party Name')),
                ('phone', models.CharField(blank=True, max_length=15, verbose_name='Party Contact Number')),
                ('address_line1', models.CharField(blank=True, max_length=100, verbose_name='Address Line 1')),
                ('address_line2', models.CharField(blank=True, max_length=100, verbose_name='Address Line 2')),
            ],
        ),
        migrations.CreateModel(
            name='StockItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, verbose_name='Enter Stock Item Name')),
                ('per', models.CharField(blank=True, choices=[('kg', 'kg'), ('pc', 'pc'), ('mtr', 'mtr')], max_length=10, verbose_name='Enter Sale Method')),
                ('hsncode', models.CharField(blank=True, max_length=5, verbose_name='Enter HSN/SAC Code')),
            ],
        ),
        migrations.CreateModel(
            name='InvoiceItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rate', models.DecimalField(decimal_places=2, max_digits=12)),
                ('quantity', models.PositiveIntegerField(default=0)),
                ('description', models.TextField(blank=True, max_length=1000)),
                ('invno', models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.DO_NOTHING, to='sales.invoice')),
                ('stockitem', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.DO_NOTHING, to='sales.stockitem')),
            ],
        ),
        migrations.AddField(
            model_name='invoice',
            name='party_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='sales.party'),
        ),
    ]