# Generated by Django 2.0.9 on 2018-11-19 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0004_auto_20180825_1642'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='characterclass',
            options={'ordering': ['name']},
        ),
        migrations.AlterModelOptions(
            name='characterfaction',
            options={'ordering': ['name']},
        ),
        migrations.AlterModelOptions(
            name='characterrace',
            options={'ordering': ['name']},
        ),
        migrations.AddField(
            model_name='playercharacter',
            name='notes',
            field=models.TextField(blank=True, null=True, verbose_name='Additional notes'),
        ),
    ]
