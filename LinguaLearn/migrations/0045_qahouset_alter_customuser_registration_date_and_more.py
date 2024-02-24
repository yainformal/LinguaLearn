# Generated by Django 4.2.10 on 2024-02-24 14:21

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("LinguaLearn", "0044_alter_customuser_registration_date_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="QAHouset",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("questions", models.TextField(blank=True, null=True)),
                ("answers", models.TextField(blank=True, null=True)),
            ],
            options={
                "db_table": "lingualearn_QA_House",
            },
        ),
        migrations.AlterField(
            model_name="customuser",
            name="registration_date",
            field=models.DateTimeField(
                default=datetime.datetime(2024, 2, 24, 17, 21, 27, 831709), null=True
            ),
        ),
        migrations.AlterField(
            model_name="dictionary",
            name="add_date",
            field=models.DateTimeField(
                db_column="add_dttm",
                default=datetime.datetime(2024, 2, 24, 17, 21, 27, 832099),
                null=True,
            ),
        ),
        migrations.CreateModel(
            name="QuestionEmbedding",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("embedding", models.BinaryField()),
                (
                    "qa_house",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="question_embedding",
                        to="LinguaLearn.qahouset",
                    ),
                ),
            ],
            options={
                "db_table": "lingualearn_QE_House",
            },
        ),
        migrations.CreateModel(
            name="AnswerEmbedding",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("embedding", models.BinaryField()),
                (
                    "qa_house",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="answer_embedding",
                        to="LinguaLearn.qahouset",
                    ),
                ),
            ],
            options={
                "db_table": "lingualearn_AE_House",
            },
        ),
    ]
