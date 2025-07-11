# Generated by Django 5.1.3 on 2025-04-30 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Colors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('UI_ID', models.CharField(max_length=255)),
                ('NAME', models.CharField(max_length=255)),
                ('RGB', models.CharField(max_length=255)),
                ('SYMBOL', models.CharField(max_length=255)),
                ('USAGE_FOR_BRANDING', models.CharField(max_length=255)),
                ('CATEGORY', models.CharField(max_length=255)),
                ('MEANING', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'verbose_name_plural': 'Colors',
            },
        ),
        migrations.DeleteModel(
            name='MyModel',
        ),
    ]
