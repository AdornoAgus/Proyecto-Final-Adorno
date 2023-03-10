# Generated by Django 4.1.6 on 2023-03-09 20:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=300)),
                ('slug', models.SlugField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=300)),
                ('slug', models.SlugField(unique=True)),
                ('overview', models.TextField()),
                ('date_created', models.DateTimeField(auto_now=True)),
                ('contenido', models.TextField()),
                ('featured', models.BooleanField(default=False)),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
                ('categorias', models.ManyToManyField(to='blogs.categoria')),
            ],
        ),
    ]
