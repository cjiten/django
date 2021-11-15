# Generated by Django 3.2.9 on 2021-11-15 15:23

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
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('cslug', models.SlugField(blank=True, max_length=255, null=True, unique=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Web',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('url', models.CharField(blank=True, max_length=255, null=True)),
                ('search_titel', models.CharField(blank=True, max_length=255, null=True)),
                ('colour', models.CharField(max_length=255)),
                ('copyright', models.CharField(max_length=255)),
                ('google_analytics', models.CharField(blank=True, max_length=5000, null=True)),
                ('google_adsense', models.CharField(blank=True, max_length=5000, null=True)),
                ('google_ads_display', models.CharField(blank=True, max_length=5000, null=True)),
                ('google_ads_in_feed', models.CharField(blank=True, max_length=5000, null=True)),
                ('google_ads_in_article', models.CharField(blank=True, max_length=5000, null=True)),
                ('google_ads_matched_content', models.CharField(blank=True, max_length=5000, null=True)),
                ('telegram', models.CharField(blank=True, max_length=1000, null=True)),
                ('github', models.CharField(blank=True, max_length=1000, null=True)),
                ('pin', models.CharField(blank=True, max_length=1000, null=True)),
                ('yt', models.CharField(blank=True, max_length=1000, null=True)),
                ('twitter', models.CharField(blank=True, max_length=1000, null=True)),
                ('fb', models.CharField(blank=True, max_length=1000, null=True)),
                ('insta', models.CharField(blank=True, max_length=1000, null=True)),
                ('discord', models.CharField(blank=True, max_length=1000, null=True)),
                ('linkden', models.CharField(blank=True, max_length=1000, null=True)),
                ('reddit', models.CharField(blank=True, max_length=1000, null=True)),
                ('feature_titel', models.CharField(blank=True, max_length=255, null=True)),
                ('feature_1', models.CharField(blank=True, max_length=255, null=True)),
                ('feature_2', models.CharField(blank=True, max_length=255, null=True)),
                ('feature_3', models.CharField(blank=True, max_length=255, null=True)),
                ('feature_4', models.CharField(blank=True, max_length=255, null=True)),
                ('feature_5', models.CharField(blank=True, max_length=255, null=True)),
                ('feature_6', models.CharField(blank=True, max_length=255, null=True)),
                ('logo', models.ImageField(blank=True, null=True, upload_to='media/')),
                ('logo_code', models.CharField(blank=True, max_length=500000, null=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('slug', models.SlugField(blank=True, max_length=255, null=True, unique=True)),
                ('board_name', models.CharField(max_length=255)),
                ('board_name_short', models.CharField(max_length=255)),
                ('post_name', models.CharField(max_length=255)),
                ('application_mode', models.CharField(choices=[('Online', 'Online'), ('Offline', 'Offline')], default=True, max_length=255)),
                ('exam_mode', models.CharField(choices=[('Offline', 'Offline'), ('Online', 'Online')], default=True, max_length=255)),
                ('web_url', models.CharField(max_length=255)),
                ('form_starting_date', models.CharField(blank=True, max_length=255, null=True)),
                ('form_last_date', models.CharField(blank=True, max_length=255, null=True)),
                ('fee_last_date', models.CharField(blank=True, max_length=255, null=True)),
                ('eligibility_criteria', models.CharField(blank=True, max_length=255, null=True)),
                ('year', models.IntegerField(blank=True, null=True)),
                ('age_limit_minimum', models.IntegerField(blank=True, null=True)),
                ('age_limit_maximum', models.IntegerField(blank=True, null=True)),
                ('number_of_post', models.IntegerField(blank=True, null=True)),
                ('general_post', models.IntegerField(blank=True, null=True)),
                ('ewc_post', models.IntegerField(blank=True, null=True)),
                ('ebc_post', models.IntegerField(blank=True, null=True)),
                ('obc_post', models.IntegerField(blank=True, null=True)),
                ('sc_post', models.IntegerField(blank=True, null=True)),
                ('st_post', models.IntegerField(blank=True, null=True)),
                ('creamylayer_post', models.IntegerField(blank=True, null=True)),
                ('general_post_application_fees', models.IntegerField(blank=True, null=True)),
                ('ewc_post_application_fees', models.IntegerField(blank=True, null=True)),
                ('ebc_post_application_fees', models.IntegerField(blank=True, null=True)),
                ('obc_post_application_fees', models.IntegerField(blank=True, null=True)),
                ('sc_post_application_fees', models.IntegerField(blank=True, null=True)),
                ('st_post_application_fees', models.IntegerField(blank=True, null=True)),
                ('creamylayer_fees', models.IntegerField(blank=True, null=True)),
                ('correction_fees', models.IntegerField(blank=True, null=True)),
                ('exam_date', models.CharField(blank=True, max_length=255, null=True)),
                ('latest_jobs', models.CharField(blank=True, max_length=2000, null=True)),
                ('syllabus', models.CharField(blank=True, max_length=2000, null=True)),
                ('previous_year_question_papers', models.CharField(blank=True, max_length=2000, null=True)),
                ('admit_card', models.CharField(blank=True, max_length=2000, null=True)),
                ('admit_card_date', models.CharField(default='Announced Soon', max_length=255)),
                ('answer_key', models.CharField(blank=True, max_length=2000, null=True)),
                ('answer_key_date', models.CharField(default='Announced Soon', max_length=255)),
                ('result', models.CharField(blank=True, max_length=2000, null=True)),
                ('result_date', models.CharField(default='Announced Soon', max_length=255)),
                ('cut_off_marks', models.CharField(blank=True, max_length=2000, null=True)),
                ('cut_off_marks_date', models.CharField(default='Announced Soon', max_length=255)),
                ('photo', models.ImageField(upload_to='media/post/%Y/%m/%d')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('created_date_only', models.DateField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('modified_date_only', models.DateField(auto_now=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
