# Generated by Django 4.2 on 2024-02-13 07:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("LinguaLearn", "0035_alter_customuser_registration_date_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customuser",
            name="registration_date",
            field=models.DateTimeField(
                default=datetime.datetime(2024, 2, 13, 10, 50, 45, 758688), null=True
            ),
        ),
        migrations.AlterField(
            model_name="dictionary",
            name="add_date",
            field=models.DateTimeField(
                db_column="add_dttm",
                default=datetime.datetime(2024, 2, 13, 10, 50, 45, 759033),
                null=True,
            ),
        ),
    ]