# Generated by Django 2.2.16 on 2022-09-25 09:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0009_auto_20210822_1842'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='user',
            name='username_is_not_me',
        ),
        migrations.AlterField(
            model_name='genretitle',
            name='title',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='reviews.Title', verbose_name='Произведение'),
        ),
    ]
