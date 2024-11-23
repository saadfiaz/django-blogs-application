# Generated by Django 5.1.2 on 2024-11-21 08:52

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Author",
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
                ("first_name", models.CharField(max_length=40)),
                ("last_name", models.CharField(max_length=40)),
                ("email_address", models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name="Tag",
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
                ("caption", models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name="Post",
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
                ("title", models.CharField(max_length=50)),
                ("excerpt", models.CharField(max_length=100)),
                ("image_name", models.CharField(max_length=50)),
                ("date", models.DateField(auto_now=True)),
                ("slug", models.SlugField(unique=True)),
                (
                    "content",
                    models.TextField(
                        validators=[django.core.validators.MinLengthValidator(10)]
                    ),
                ),
                (
                    "author",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="Posts",
                        to="blog.author",
                    ),
                ),
                ("tags", models.ManyToManyField(to="blog.tag")),
            ],
        ),
    ]
