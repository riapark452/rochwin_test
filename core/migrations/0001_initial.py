# Generated by Django 4.2.7 on 2023-11-29 11:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('update_at', models.DateTimeField(auto_created=True, auto_now_add=True)),
                ('created_at', models.DateTimeField(auto_created=True, auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('full_name', models.CharField()),
                ('birthdate', models.DateField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('update_at', models.DateTimeField(auto_created=True, auto_now_add=True)),
                ('created_at', models.DateTimeField(auto_created=True, auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('full_name', models.CharField()),
                ('birthdate', models.DateField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('update_at', models.DateTimeField(auto_created=True, auto_now_add=True)),
                ('created_at', models.DateTimeField(auto_created=True, auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('name', models.CharField()),
                ('quantity', models.IntegerField()),
                ('price', models.FloatField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('update_at', models.DateTimeField(auto_created=True, auto_now_add=True)),
                ('created_at', models.DateTimeField(auto_created=True, auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('price', models.FloatField()),
                ('date', models.DateTimeField()),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.client')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.employee')),
                ('products', models.ManyToManyField(to='core.product')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]