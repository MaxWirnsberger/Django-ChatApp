# Generated by Django 5.0.2 on 2024-02-23 09:34

import datetime
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=500)),
                ('created_at', models.DateField(default=datetime.date.today)),
                ('receiver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='receiver_message_set', to=settings.AUTH_USER_MODEL)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='author_message_set', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
