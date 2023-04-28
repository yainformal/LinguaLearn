# Generated by Django 4.2 on 2023-04-27 21:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("LinguaLearn", "0010_alter_customuser_registration_date"),
    ]

    operations = [
        migrations.RemoveField(model_name="dictionary", name="card_img",),
        migrations.RemoveField(model_name="dictionary", name="speech",),
        migrations.AlterField(
            model_name="customuser",
            name="registration_date",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 4, 28, 0, 47, 30, 71733), null=True
            ),
        ),
        migrations.AlterField(
            model_name="dictionary",
            name="add_date",
            field=models.DateTimeField(
                db_column="add_dttm",
                default=datetime.datetime(2023, 4, 28, 0, 47, 30, 71882),
            ),
        ),
    ]
