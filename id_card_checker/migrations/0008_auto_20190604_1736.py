# Generated by Django 2.2.1 on 2019-06-04 15:36

from django.db import migrations, models
import id_card_checker.validators


class Migration(migrations.Migration):

    dependencies = [
        ('id_card_checker', '0007_auto_20190517_0023'),
    ]

    operations = [
        migrations.AlterField(
            model_name='idcard',
            name='document',
            field=models.ImageField(blank=True, upload_to='temp_docs', validators=[id_card_checker.validators.validate_file_size], verbose_name="copie de la pièce d'identité"),
        ),
    ]
