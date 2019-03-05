# Generated by Django 2.1.7 on 2019-03-05 17:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Titre de la catégorie')),
            ],
        ),
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Libellé du choix')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(max_length=10000, verbose_name='Texte du commentaire')),
                ('publication_date', models.DateTimeField(auto_now_add=True, verbose_name='Date de publication du commentaire')),
                ('last_update', models.DateTimeField(auto_now=True, verbose_name='Date de dernière mise à jour du commentaire')),
                ('visible', models.BooleanField(default=True, verbose_name='Visible')),
            ],
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Referendum',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300, verbose_name='Titre du référendum')),
                ('description', models.TextField(max_length=10000, verbose_name='Description du référendum')),
                ('question', models.CharField(max_length=300, verbose_name='Question posée aux citoyens')),
                ('creation_date', models.DateTimeField(auto_now_add=True, verbose_name='Date de création')),
                ('last_update', models.DateTimeField(auto_now=True, verbose_name='Date de la dernière modification')),
                ('publication_date', models.DateTimeField(blank=True, verbose_name='Date de publication')),
                ('event_start', models.DateTimeField(blank=True, verbose_name='Début des votes')),
                ('event_end', models.DateTimeField(blank=True, verbose_name='Fin des votes')),
                ('Category', models.ManyToManyField(to='referendum.Category')),
            ],
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(max_length=1000, verbose_name='Raison du signalement')),
                ('creation_date', models.DateTimeField(auto_now_add=True, verbose_name='Date de création')),
                ('comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='referendum.Comment', verbose_name='Commentaire signalé')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Citoyen')),
            ],
        ),
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vote_date', models.DateTimeField(auto_now_add=True, verbose_name='Date de vote')),
                ('choice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='referendum.Choice', verbose_name='Valeur du vote')),
                ('referendum', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='referendum.Referendum', verbose_name='Référendum')),
            ],
        ),
        migrations.CreateModel(
            name='VoteToken',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.CharField(max_length=150, verbose_name='Token')),
                ('voted', models.BooleanField(default=False, verbose_name='A voté ?')),
                ('referendum', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='referendum.Referendum', verbose_name='Référendum')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Citoyen')),
            ],
        ),
        migrations.AddField(
            model_name='like',
            name='referendum',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='referendum.Referendum', verbose_name='Référendum'),
        ),
        migrations.AddField(
            model_name='like',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Citoyen'),
        ),
        migrations.AddField(
            model_name='comment',
            name='referendum',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='referendum.Referendum', verbose_name='Référendum'),
        ),
        migrations.AddField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Citoyen'),
        ),
        migrations.AddField(
            model_name='choice',
            name='referendum',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='referendum.Referendum', verbose_name='Référendum'),
        ),
    ]