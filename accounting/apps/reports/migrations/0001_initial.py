# Generated by Django 3.1.7 on 2021-03-31 09:10

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PayRunSettings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('salaries_follow_profits', models.BooleanField(default=False)),
                ('payrun_period', models.CharField(choices=[('monthly', 'monthly')], default='monthly', max_length=20, verbose_name='Payrun Period')),
                ('organization', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='payrun_settings', to='books.organization')),
            ],
        ),
        migrations.CreateModel(
            name='FinancialSettings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('financial_year_end_day', models.PositiveSmallIntegerField(default=31, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(31)])),
                ('financial_year_end_month', models.PositiveSmallIntegerField(default=12, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(12)])),
                ('tax_id_number', models.CharField(blank=True, max_length=150, null=True)),
                ('tax_id_display_name', models.CharField(blank=True, max_length=150, null=True)),
                ('tax_period', models.CharField(choices=[('monthly', '1 month'), ('bimonthly', '2 months'), ('quarter', '3 months'), ('half', '6 months'), ('year', '1 year')], max_length=20, verbose_name='Tax Period')),
                ('organization', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='financial_settings', to='books.organization')),
            ],
        ),
        migrations.CreateModel(
            name='BusinessSettings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('business_type', models.CharField(choices=[('sole_proprietorship', 'Sole Proprietorship'), ('partnership', 'Partnership'), ('corporation', 'Corporation')], max_length=50)),
                ('organization', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='business_settings', to='books.organization')),
            ],
        ),
    ]
