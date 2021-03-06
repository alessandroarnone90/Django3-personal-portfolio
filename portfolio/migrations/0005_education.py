# Generated by Django 3.0.5 on 2020-04-19 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0004_auto_20200419_0935'),
    ]

    operations = [
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('school', models.CharField(max_length=20)),
                ('description', models.TextField()),
                ('placeCity', models.CharField(max_length=20)),
                ('placeCountry', models.CharField(max_length=20)),
                ('dateStart', models.DateField()),
                ('dateEnd', models.DateField()),
                ('finalProject', models.CharField(max_length=100)),
            ],
        ),
    ]
