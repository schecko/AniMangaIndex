# Generated by Django 2.0.7 on 2018-07-21 21:04

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Content',
            fields=[
                ('contentID', models.IntegerField(primary_key=True, serialize=False)),
                ('type', models.IntegerField(choices=[(0, 'Manga'), (1, 'Book'), (2, 'Anime')])),
                ('title', models.CharField(max_length=255)),
                ('complete', models.BooleanField()),
                ('rating', models.IntegerField(validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(0)])),
                ('date', models.DateField()),
                ('genre', models.IntegerField(choices=[(0, 'Mystery'), (1, 'Drama'), (2, 'SciFi'), (3, 'Action'), (4, 'Fantasy'), (5, 'Comedy')])),
                ('source', models.IntegerField(choices=[(0, 'Manga'), (1, 'Book'), (2, 'Anime')])),
            ],
        ),
        migrations.CreateModel(
            name='Create',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.IntegerField(choices=[(0, 'Artist'), (1, 'Director'), (2, 'Animator'), (3, 'Author')])),
                ('content', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Content')),
            ],
        ),
        migrations.CreateModel(
            name='Creator',
            fields=[
                ('creatorID', models.IntegerField(primary_key=True, serialize=False)),
                ('birthday', models.DateField()),
                ('gender', models.BooleanField()),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='FavoriteContent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contentID', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='main.Content')),
            ],
        ),
        migrations.CreateModel(
            name='Hire',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='main.Creator')),
            ],
        ),
        migrations.CreateModel(
            name='License',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('publisher', models.CharField(max_length=255)),
                ('contentID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Content')),
            ],
        ),
        migrations.CreateModel(
            name='Studio',
            fields=[
                ('name', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('founded', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('userID', models.IntegerField(primary_key=True, serialize=False)),
                ('privileges', models.BooleanField()),
                ('password', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='VolumeSeason',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num', models.IntegerField()),
                ('title', models.CharField(max_length=225)),
                ('contentID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Content')),
            ],
        ),
        migrations.AddField(
            model_name='license',
            name='studio',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='main.Studio'),
        ),
        migrations.AddField(
            model_name='hire',
            name='studio',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='main.Studio'),
        ),
        migrations.AddField(
            model_name='favoritecontent',
            name='userID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='main.User'),
        ),
        migrations.AddField(
            model_name='create',
            name='creator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='main.Creator'),
        ),
        migrations.AlterUniqueTogether(
            name='volumeseason',
            unique_together={('contentID', 'num')},
        ),
        migrations.AlterUniqueTogether(
            name='license',
            unique_together={('contentID', 'studio')},
        ),
        migrations.AlterUniqueTogether(
            name='hire',
            unique_together={('studio', 'creator')},
        ),
        migrations.AlterUniqueTogether(
            name='favoritecontent',
            unique_together={('userID', 'contentID')},
        ),
        migrations.AlterUniqueTogether(
            name='create',
            unique_together={('content', 'creator')},
        ),
    ]
