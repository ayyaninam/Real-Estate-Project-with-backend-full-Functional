# Generated by Django 3.2.8 on 2021-10-27 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estate', '0007_dealer_register_id_of'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dealer_register',
            name='id_of',
        ),
        migrations.AddField(
            model_name='dealer_register',
            name='request_by',
            field=models.CharField(default='', max_length=300),
            preserve_default=False,
        ),
    ]
