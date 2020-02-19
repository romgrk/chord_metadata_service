# Generated by Django 2.2.9 on 2020-02-17 21:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chord', '0007_auto_20200129_1537'),
    ]

    operations = [
        migrations.AddField(
            model_name='dataset',
            name='version',
            field=models.CharField(blank=True, default='version_2020-02-17 16:47:59.425036', help_text='A release point for the dataset when applicable.', max_length=200),
        ),
    ]
