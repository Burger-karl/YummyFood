# Generated by Django 3.1 on 2023-07-20 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='pizza',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('priceM', models.DecimalField(decimal_places=2, max_digits=4)),
                ('priceL', models.DecimalField(decimal_places=2, max_digits=4)),
                ('pImage', models.URLField()),
            ],
        ),
    ]
