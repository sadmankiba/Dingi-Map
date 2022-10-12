# Generated by Django 2.1.4 on 2019-02-14 05:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ServiceRatings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)])),
            ],
        ),
        migrations.AlterField(
            model_name='services',
            name='service_type',
            field=models.CharField(choices=[('electricity', 'Electricity'), ('plumber', 'Plumber')], default='Electricity', max_length=30),
        ),
        migrations.AddField(
            model_name='serviceratings',
            name='service',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.Services'),
        ),
        migrations.AddField(
            model_name='serviceratings',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
