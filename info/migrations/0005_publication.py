# Generated by Django 3.1 on 2020-09-15 15:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0004_auto_20200810_1358'),
    ]

    operations = [
        migrations.CreateModel(
            name='Publication',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='title')),
                ('author', models.TextField(verbose_name='author')),
                ('publisher', models.CharField(max_length=200, null=True, verbose_name='journal')),
                ('year', models.IntegerField(verbose_name='year')),
                ('arxiv_url', models.URLField(null=True, verbose_name='arxiv')),
                ('ads_url', models.URLField(null=True, verbose_name='ADS')),
                ('pdf_file', models.FileField(null=True, upload_to='publications/', verbose_name='pdf file')),
                ('prime_author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='info.teammember')),
            ],
        ),
    ]
