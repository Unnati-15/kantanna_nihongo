# Generated by Django 4.1.1 on 2024-04-13 08:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='QuizQuestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField()),
                ('opt1', models.CharField(max_length=80)),
                ('opt2', models.CharField(max_length=80)),
                ('opt3', models.CharField(max_length=80)),
                ('opt4', models.CharField(max_length=80)),
                ('level', models.CharField(max_length=80)),
                ('time_limit', models.IntegerField()),
                ('right_ans', models.CharField(max_length=80)),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quiz.quiztype')),
            ],
        ),
    ]
