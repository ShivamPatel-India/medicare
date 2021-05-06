# Generated by Django 3.1.5 on 2021-04-09 11:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Citie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city_name', models.CharField(max_length=400)),
            ],
        ),
        migrations.CreateModel(
            name='Condition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('condition_name', models.CharField(max_length=400)),
                ('overview', models.TextField(max_length=1000)),
                ('symptoms', models.TextField(max_length=1000)),
                ('causes', models.TextField(max_length=1000)),
                ('complications', models.TextField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department_name', models.CharField(max_length=400)),
            ],
        ),
        migrations.CreateModel(
            name='Hospital',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hospital_name', models.CharField(max_length=400)),
                ('address', models.TextField(default='', max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Procedure',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('procedure_name', models.CharField(max_length=400)),
                ('overview', models.TextField(max_length=1000)),
                ('why_its_done', models.TextField(max_length=1000)),
                ('risks', models.TextField(max_length=1000)),
                ('results', models.TextField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('profile_picture', models.ImageField(blank=True, default='default.jpg', max_length=500, null=True, upload_to='Doctors/profile_img')),
                ('area_of_focus', models.TextField(max_length=1000)),
                ('bio', models.TextField(max_length=1000)),
                ('education', models.TextField(max_length=1000)),
                ('awards', models.TextField(max_length=1000)),
                ('city', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='doctors.citie')),
                ('condition_trated', models.ManyToManyField(default='', to='doctors.Condition')),
                ('department', models.ManyToManyField(default='', to='doctors.Department')),
                ('hospital', models.ManyToManyField(default='', to='doctors.Hospital')),
                ('procedures_performed', models.ManyToManyField(default='', to='doctors.Procedure')),
            ],
        ),
    ]