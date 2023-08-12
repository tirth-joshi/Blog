from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0005_remove_like_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='like',
            name='blog',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='catalog.blog'),
        ),
    ]
