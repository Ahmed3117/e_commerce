# Generated by Django 3.2 on 2022-09-02 23:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0027_alter_rating_date_added'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rating',
            name='review',
            field=models.CharField(default='no review comment', max_length=300),
        ),
    ]
