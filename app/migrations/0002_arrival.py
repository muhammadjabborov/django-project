# Generated by Django 4.1.2 on 2022-10-18 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Arrival',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('image', models.ImageField(upload_to='image/')),
                ('rating', models.CharField(choices=[('Good', 'Good'), ('Bad', 'Bad'), ('50/50', 'Fifty To Fifty')], default='Good', max_length=255)),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('price', models.FloatField()),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
