# Generated by Django 3.2 on 2023-03-30 08:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0002_review_score'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='score',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='reviews.rating'),
        ),
    ]
