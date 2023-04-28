# Generated by Django 4.2 on 2023-04-28 18:02

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("LinguaLearn", "0021_alter_customuser_registration_date_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customersession",
            name="end_dttm",
            field=models.DateTimeField(default="31.12.5999"),
        ),
        migrations.AlterField(
            model_name="customuser",
            name="registration_date",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 4, 28, 21, 2, 52, 717033), null=True
            ),
        ),
        migrations.AlterField(
            model_name="dictionary",
            name="add_date",
            field=models.DateTimeField(
                db_column="add_dttm",
                default=datetime.datetime(2023, 4, 28, 21, 2, 52, 717179),
                null=True,
            ),
        ),
    ]
