from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_blog_like'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='like',
            name='post',
        ),
        migrations.RemoveField(
            model_name='like',
            name='user',
        ),
    ]
