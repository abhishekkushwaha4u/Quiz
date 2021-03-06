# Generated by Django 2.1.5 on 2019-05-10 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='improved_question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(blank=True, max_length=300)),
                ('question_img', models.FileField(blank=True, null=True, upload_to='')),
                ('answer', models.CharField(blank=True, max_length=10)),
                ('a', models.CharField(blank=True, max_length=200)),
                ('a_img', models.FileField(blank=True, null=True, upload_to='')),
                ('b', models.CharField(blank=True, max_length=200)),
                ('b_img', models.FileField(blank=True, null=True, upload_to='')),
                ('c', models.CharField(blank=True, max_length=200)),
                ('c_img', models.FileField(blank=True, null=True, upload_to='')),
                ('d', models.CharField(blank=True, max_length=200)),
                ('d_img', models.FileField(blank=True, null=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='multiple_choice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_number', models.IntegerField()),
                ('question', models.CharField(max_length=300)),
                ('answer', models.CharField(max_length=10)),
                ('a', models.CharField(max_length=200)),
                ('b', models.CharField(max_length=200)),
                ('c', models.CharField(max_length=200)),
                ('d', models.CharField(max_length=200)),
            ],
        ),
    ]
