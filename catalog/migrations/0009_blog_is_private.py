from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0008_remove_blog_type_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='is_private',
            field=models.BooleanField(default=False),
        ),
    ]
