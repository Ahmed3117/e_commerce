# Generated by Django 3.2 on 2022-09-06 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0028_alter_rating_review'),
    ]

    operations = [
        migrations.AddField(
            model_name='pill',
            name='paid',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='pill',
            name='status',
            field=models.CharField(choices=[('delivered', 'delivered'), ('underdeliver', 'underdeliver'), ('waiting', 'waiting')], default='waiting', max_length=50),
        ),
    ]
