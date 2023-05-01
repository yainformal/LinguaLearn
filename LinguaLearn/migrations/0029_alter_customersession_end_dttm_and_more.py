# Generated by Django 4.2 on 2023-05-01 13:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("LinguaLearn", "0028_alter_customuser_registration_date_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customersession",
            name="end_dttm",
            field=models.DateTimeField(default="5999-12-31 00:00:00"),
        ),
        migrations.AlterField(
            model_name="customuser",
            name="registration_date",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 5, 1, 16, 29, 22, 480741), null=True
            ),
        ),
        migrations.AlterField(
            model_name="dictionary",
            name="add_date",
            field=models.DateTimeField(
                db_column="add_dttm",
                default=datetime.datetime(2023, 5, 1, 16, 29, 22, 481073),
                null=True,
            ),
        ),
    ]
