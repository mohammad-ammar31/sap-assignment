# Generated by Django 4.0.6 on 2022-07-29 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('foodName', models.CharField(max_length=100)),
                ('foodType', models.CharField(max_length=100)),
                ('pinCode', models.IntegerField(default=0)),
            ],
        ),
    ]