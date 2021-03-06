# Generated by Django 3.1.5 on 2021-01-29 19:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, default='', max_length=200, null=True)),
                ('status', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Categorie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Supplement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=2, max_digits=500)),
                ('description', models.TextField(blank=True, default='', max_length=1000, null=True)),
                ('image_1', models.ImageField(blank=True, default='default.jpg', null=True, upload_to='Supplements/img')),
                ('image_2', models.ImageField(blank=True, default='default.jpg', null=True, upload_to='Supplements/img')),
                ('image_3', models.ImageField(blank=True, default='default.jpg', null=True, upload_to='Supplements/img')),
                ('ingredients', models.TextField(blank=True, max_length=1000, null=True)),
                ('benefits', models.TextField(blank=True, max_length=1000, null=True)),
                ('offer', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=100, null=True)),
                ('direction', models.TextField(blank=True, max_length=1000, null=True)),
                ('status', models.BooleanField(default=True)),
                ('brand', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='store.brand')),
                ('category', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='store.categorie')),
            ],
        ),
        migrations.CreateModel(
            name='Equipment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=2, max_digits=500)),
                ('description', models.TextField(blank=True, default='', max_length=200, null=True)),
                ('image_1', models.ImageField(default='default.jpg', max_length=5, upload_to='Equipments/img')),
                ('image_2', models.ImageField(default='default.jpg', max_length=5, upload_to='Equipments/img')),
                ('image_3', models.ImageField(default='default.jpg', max_length=5, upload_to='Equipments/img')),
                ('offer', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=100, null=True)),
                ('uses', models.TextField(max_length=200)),
                ('status', models.BooleanField(default=True)),
                ('brand', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='store.brand')),
                ('category', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='store.categorie')),
            ],
        ),
    ]
