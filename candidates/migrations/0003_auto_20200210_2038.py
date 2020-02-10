# Generated by Django 3.0.3 on 2020-02-10 20:38

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('candidates', '0002_auto_20200210_1610'),
    ]

    operations = [
        migrations.AlterField(
            model_name='score',
            name='candidate',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='scores', to='candidates.Candidate'),
        ),
        migrations.AlterField(
            model_name='score',
            name='score',
            field=models.FloatField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)]),
        ),
    ]
