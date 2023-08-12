from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=180, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('content', models.CharField(blank=True, max_length=180, null=True)),
                ('creation_date', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=180, null=True)),
                ('type', models.CharField(blank=True, max_length=180, null=True)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='catalog.blog')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
