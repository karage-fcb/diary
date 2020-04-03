# Generated by Django 3.0.4 on 2020-04-01 05:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('diaryapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='diarymodel',
            name='submitter',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='投稿者'),
            preserve_default=False,
        ),
    ]