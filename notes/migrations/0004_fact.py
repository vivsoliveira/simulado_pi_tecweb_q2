# Generated by Django 5.0.3 on 2024-03-26 23:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0003_tag_alter_note_id_note_tag'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.TextField()),
                ('curtidas', models.IntegerField(default=0)),
            ],
        ),
    ]
