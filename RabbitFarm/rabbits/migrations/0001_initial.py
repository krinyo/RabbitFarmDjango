# Generated by Django 5.0 on 2023-12-22 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Rabbit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('age', models.PositiveIntegerField(verbose_name='Age')),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1, verbose_name='Gender')),
                ('color', models.CharField(max_length=50, verbose_name='Color')),
                ('weight', models.FloatField(verbose_name='Weight')),
                ('birth_date', models.DateField(verbose_name='Birth Date')),
                ('date_acquired', models.DateField(verbose_name='Date Acquired')),
                ('notes', models.TextField(blank=True, null=True, verbose_name='Notes')),
            ],
            options={
                'verbose_name': 'Rabbit',
                'verbose_name_plural': 'Rabbits',
            },
        ),
    ]