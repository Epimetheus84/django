# Generated by Django 2.1.3 on 2018-11-17 10:30

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place', models.IntegerField()),
                ('user_name', models.CharField(max_length=30)),
                ('user_phone', models.CharField(max_length=30)),
                ('user_email', models.CharField(max_length=30, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='seance',
            name='time',
            field=models.TimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ticket',
            name='hall',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.Seance'),
        ),
    ]