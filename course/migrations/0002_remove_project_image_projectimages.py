# Generated by Django 4.1.7 on 2024-02-14 06:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='image',
        ),
        migrations.CreateModel(
            name='ProjectImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.CharField(max_length=100)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.project')),
            ],
        ),
    ]