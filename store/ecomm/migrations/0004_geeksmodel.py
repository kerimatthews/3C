# Generated by Django 4.2.2 on 2023-06-29 00:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecomm', '0003_delete_ad_delete_category_computer_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='GeeksModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
            ],
        ),
    ]