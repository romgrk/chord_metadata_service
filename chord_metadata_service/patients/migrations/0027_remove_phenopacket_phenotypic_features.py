# Generated by Django 2.2.6 on 2019-10-15 22:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0026_phenopacket_subject'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='phenopacket',
            name='phenotypic_features',
        ),
    ]