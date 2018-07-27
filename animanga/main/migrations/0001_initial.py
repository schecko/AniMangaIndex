# Generated by Django 2.0.7 on 2018-07-26 06:27

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
                ('date', models.IntegerField()),
                ('genre', models.IntegerField(choices=[(0, 'Mystery'), (1, 'Drama'), (2, 'SciFi'), (3, 'Action'), (4, 'Fantasy'), (5, 'Comedy'), (6, 'Mecha')])),
                ('source', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.Content')),
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
                ('birthday', models.IntegerField()),
                ('gender', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='FavoriteContent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contentID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Content')),
            ],
        ),
        migrations.CreateModel(
            name='Hire',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Creator')),
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
                ('founded', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('userID', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('privileges', models.BooleanField()),
                ('password', models.CharField(max_length=255)),
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
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Studio'),
        ),
        migrations.AddField(
            model_name='hire',
            name='studio',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Studio'),
        ),
        migrations.AddField(
            model_name='favoritecontent',
            name='userID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.User'),
        ),
        migrations.AddField(
            model_name='create',
            name='creator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Creator'),
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
