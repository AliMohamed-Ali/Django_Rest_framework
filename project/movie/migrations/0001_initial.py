# Generated by Django 3.2.9 on 2021-11-14 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'ordering': ('-name',),
            },
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('release_date', models.DateField()),
                ('poster', models.ImageField(upload_to='movie_poster')),
                ('watch_count', models.IntegerField()),
                ('likes', models.IntegerField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Series',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('release_date', models.DateField()),
                ('poster', models.ImageField(upload_to='movie_poster')),
                ('watch_count', models.IntegerField()),
                ('likes', models.IntegerField()),
                ('season', models.CharField(max_length=50)),
                ('episode', models.CharField(max_length=50)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
