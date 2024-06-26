# Generated by Django 5.0.4 on 2024-04-28 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_account_puzzles_finished'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='solved_puzzles',
            field=models.BinaryField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='account',
            name='puzzles_finished',
            field=models.IntegerField(default='0'),
        ),
    ]
