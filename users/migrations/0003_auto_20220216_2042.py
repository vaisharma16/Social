# Generated by Django 3.0.3 on 2022-02-16 15:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0002_auto_20220216_1305'),
    ]

    operations = [
        migrations.AlterField(
            model_name='friendrequest',
            name='from_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='from_users', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='friendrequest',
            name='to_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='to_users', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='profile',
            name='Institute_Area',
            field=models.CharField(blank=True, default=' ', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='Institute_Name',
            field=models.CharField(blank=True, default=' ', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='phone',
            field=models.DecimalField(blank=True, decimal_places=0, default=0, max_digits=10, null=True),
        ),
    ]
