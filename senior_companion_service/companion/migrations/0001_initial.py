# Generated by Django 4.2.4 on 2023-10-14 17:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Companion',
            fields=[
                ('idCompanion', models.AutoField(primary_key=True, serialize=False)),
                ('stateAvailability', models.CharField(choices=[('available', 'Available'), ('not available', 'Not Available'), ('pause', 'Pause'), ('blocked', 'Blocked')], max_length=15, null=True)),
                ('hourlyRate', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
                ('personalDescription', models.TextField(null=True)),
                ('idUser', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='authentication.user')),
            ],
        ),
    ]
