# Generated by Django 3.1.7 on 2021-03-05 06:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('report_count', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='TripReport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_trip', models.DateField()),
                ('location', models.CharField(db_index=True, max_length=50)),
                ('url', models.TextField()),
                ('text', models.TextField()),
                ('distance', models.DecimalField(decimal_places=1, max_digits=4)),
                ('duration', models.TimeField()),
                ('elevation', models.IntegerField()),
                ('display_img', models.ImageField(upload_to='')),
                ('images_count', models.IntegerField()),
                ('activity', models.TextField()),
                ('terrain_class', models.IntegerField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.author')),
            ],
        ),
    ]
