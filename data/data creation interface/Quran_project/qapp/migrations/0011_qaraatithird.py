# Generated by Django 4.2.3 on 2024-04-01 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qapp', '0010_qaraatisecond'),
    ]

    operations = [
        migrations.CreateModel(
            name='QaraatiThird',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pq_id', models.TextField()),
                ('context', models.TextField()),
                ('question', models.TextField()),
                ('answer', models.TextField(default='')),
            ],
        ),
    ]