# Generated by Django 4.2.2 on 2023-12-05 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_newsstory_image_url_alter_newsstory_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='StoryCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CatStory', models.CharField(choices=[('BL', 'Blog'), ('N', 'In the News'), ('W', 'Wins Wall')], default='BL', max_length=20)),
            ],
        ),
    ]
