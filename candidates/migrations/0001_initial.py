# Generated by Django 3.0.3 on 2020-02-09 17:23

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Candidate',
            fields=[
                ('name', models.CharField(max_length=200)),
                ('candidate_ref', models.CharField(max_length=8, primary_key=True, serialize=False, unique=True, validators=[django.core.validators.RegexValidator(code='nomatch', message='Candidate Reference must be 8 alphanumeric characters.', regex='^\\w{8}$')])),
            ],
        ),
        migrations.CreateModel(
            name='Score',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.FloatField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MinValueValidator(100)])),
                ('candidate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='candidates.Candidate')),
            ],
        ),
    ]