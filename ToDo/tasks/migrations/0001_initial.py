# Generated by Django 3.1.5 on 2021-03-05 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tasks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task', models.CharField(max_length=150)),
            ],
            options={
                'verbose_name_plural': 'Tasks',
            },
        ),
    ]
