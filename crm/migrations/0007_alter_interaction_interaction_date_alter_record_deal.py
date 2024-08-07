# Generated by Django 5.0.6 on 2024-06-30 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0006_record_deal_close_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='interaction',
            name='interaction_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='record',
            name='deal',
            field=models.CharField(blank=True, choices=[('won', 'won'), ('lost', 'lost'), ('wip', 'wip'), ('interested', 'interested')], default='wip', max_length=50, null=True),
        ),
    ]
