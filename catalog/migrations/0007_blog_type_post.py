from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0006_like_blog'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='type_post',
            field=models.CharField(choices=[('PB', 'Public'), ('PR', 'Private')], default='PB', max_length=2),
        ),
    ]
