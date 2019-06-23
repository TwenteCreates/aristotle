# Generated by Django 2.1.3 on 2018-12-02 11:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('analytics', '0010_primaryschool'),
    ]

    operations = [
        migrations.AddField(
            model_name='concept',
            name='next',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='comes_after', to='analytics.Concept'),
            preserve_default=False,
        ),
    ]
