# Generated by Django 4.0.8 on 2022-10-27 07:38

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0008_alter_contestlikes_contest_alter_contestlikes_user"),
    ]

    operations = [
        migrations.AddField(
            model_name="contestlikes",
            name="created_at",
            field=models.DateTimeField(
                auto_now_add=True,
                default=django.utils.timezone.now,
                verbose_name="建立時間",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="contestlikes",
            name="updated_at",
            field=models.DateTimeField(auto_now=True, verbose_name="更新時間"),
        ),
    ]
