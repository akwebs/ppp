# Generated by Django 4.1.3 on 2022-11-13 06:34

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_blogcategory_contact_projects_blog_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='add_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]