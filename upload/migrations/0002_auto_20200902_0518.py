# Generated by Django 3.1 on 2020-09-02 05:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploadcriminal',
            name='state',
            field=models.ForeignKey(default=11, on_delete=django.db.models.deletion.CASCADE, to='upload.states'),
        ),
    ]
