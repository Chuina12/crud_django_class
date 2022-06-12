# Generated by Django 3.2.10 on 2022-06-11 22:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Produit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_produit', models.CharField(max_length=50)),
                ('prix', models.IntegerField()),
                ('image', models.ImageField(upload_to='image')),
                ('description', models.TextField()),
            ],
        ),
    ]