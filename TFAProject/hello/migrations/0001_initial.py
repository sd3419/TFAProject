# Generated by Django 3.1.7 on 2021-04-15 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='squirrel_data',
            fields=[
                ('x', models.FloatField()),
                ('y', models.FloatField()),
                ('unique_squirrel_id', models.CharField(max_length=256, primary_key=True, serialize=False, unique=True)),
                ('hectare', models.CharField(max_length=256)),
                ('shift', models.CharField(choices=[('AM', 'AM'), ('PM', 'PM')], max_length=2)),
                ('date', models.DateField(max_length=256)),
                ('hectare_squirrel_number', models.IntegerField()),
                ('age', models.CharField(blank=True, choices=[('Adult', 'Adult'), ('Juvenile', 'Juvenile'), ('', 'blank')], max_length=256, null=True)),
                ('primary_fur_color', models.CharField(blank=True, max_length=256, null=True)),
                ('highlight_fur_color', models.CharField(blank=True, max_length=256, null=True)),
                ('combination_of_primary_and_highlight_color', models.CharField(max_length=256)),
                ('color_notes', models.CharField(blank=True, max_length=256, null=True)),
                ('location', models.CharField(blank=True, choices=[('Above Ground', 'Above Ground'), ('Ground Plane', 'Ground Plane'), ('', 'blank')], max_length=256, null=True)),
                ('above_ground_sighter_measurement', models.CharField(blank=True, max_length=256, null=True)),
                ('specific_location', models.CharField(blank=True, max_length=256, null=True)),
                ('running', models.BooleanField()),
                ('chasing', models.BooleanField()),
                ('climbing', models.BooleanField()),
                ('eating', models.BooleanField()),
                ('foraging', models.BooleanField()),
                ('other_activities', models.CharField(blank=True, max_length=256, null=True)),
                ('kuks', models.BooleanField()),
                ('quaas', models.BooleanField()),
                ('moans', models.BooleanField()),
                ('tail_flags', models.BooleanField()),
                ('tail_twitches', models.BooleanField()),
                ('approaches', models.BooleanField()),
                ('indifferent', models.BooleanField()),
                ('runs_from', models.BooleanField()),
                ('other_interactions', models.CharField(blank=True, max_length=256, null=True)),
            ],
        ),
    ]
