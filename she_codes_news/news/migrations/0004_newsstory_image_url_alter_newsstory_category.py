# Generated by Django 4.2.2 on 2023-12-02 02:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_newsstory_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='newsstory',
            name='image_url',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='newsstory',
            name='category',
            field=models.CharField(choices=[('blog', 'Blog'), ('news', 'In the News'), ('wins', 'Wins Wall')], default='blog ', max_length=10),
        ),
    ]
