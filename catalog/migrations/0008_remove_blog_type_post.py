from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0007_blog_type_post'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='type_post',
        ),
    ]
