# Generated by Django 4.2.6 on 2023-10-20 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Site_admin', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='category_tb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Category_Name', models.CharField(max_length=20)),
            ],
        ),
    ]