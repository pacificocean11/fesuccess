# Generated by Django 3.2.9 on 2021-12-16 14:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0016_auto_20211216_1433'),
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('country', django_countries.fields.CountryField(max_length=2)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('purchase_time', models.DateTimeField(blank=True)),
                ('package_expiration_time', models.DateTimeField(blank=True)),
                ('discipline', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.discipline')),
                ('order_details', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='blog.orderdetail')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
