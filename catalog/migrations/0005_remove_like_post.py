from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_blog_user_like_post'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='like',
            name='post',
        ),
    ]
