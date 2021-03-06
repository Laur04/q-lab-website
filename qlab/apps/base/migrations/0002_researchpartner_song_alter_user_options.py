# Generated by Django 4.0.5 on 2022-06-14 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ResearchPartner',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=50)),
                ('artist_name', models.CharField(max_length=50)),
                ('link', models.URLField()),
            ],
        ),
        migrations.AlterModelOptions(
            name='user',
            options={'ordering': ('last_name', 'first_name')},
        ),
    ]
