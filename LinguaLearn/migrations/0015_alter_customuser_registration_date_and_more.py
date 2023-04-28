# Generated by Django 4.2 on 2023-04-27 21:52

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("LinguaLearn", "0014_alter_customuser_registration_date_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customuser",
            name="registration_date",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 4, 28, 0, 52, 4, 230067), null=True
            ),
        ),
        migrations.AlterField(
            model_name="dictionary",
            name="add_date",
            field=models.DateTimeField(
                db_column="add_dttm",
                default=datetime.datetime(2023, 4, 28, 0, 52, 4, 230209),
            ),
        ),
        migrations.AlterField(
            model_name="dictionary",
            name="customer_added",
            field=models.ForeignKey(
                default=-1,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                to="LinguaLearn.customuser",
            ),
        ),
    ]
