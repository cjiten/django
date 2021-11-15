from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Web(models.Model):
    name = models.CharField(max_length=255)
    url = models.CharField(max_length=255, null=True, blank=True)
    search_titel = models.CharField(max_length=255, null=True, blank=True)
    colour = models.CharField(max_length=255)
    copyright = models.CharField(max_length=255)
    google_analytics = models.CharField(max_length=5000, null=True, blank=True)
    google_adsense = models.CharField(max_length=5000, null=True, blank=True)
    google_ads_display = models.CharField(max_length=5000, null=True, blank=True)
    google_ads_in_feed = models.CharField(max_length=5000, null=True, blank=True)
    google_ads_in_article = models.CharField(max_length=5000, null=True, blank=True)
    google_ads_matched_content = models.CharField(max_length=5000, null=True, blank=True)
    telegram = models.CharField(max_length=1000, null=True, blank=True)
    github = models.CharField(max_length=1000, null=True, blank=True)
    pin = models.CharField(max_length=1000, null=True, blank=True)
    yt = models.CharField(max_length=1000, null=True, blank=True)
    twitter = models.CharField(max_length=1000, null=True, blank=True)
    fb = models.CharField(max_length=1000, null=True, blank=True)
    insta = models.CharField(max_length=1000, null=True, blank=True)
    discord = models.CharField(max_length=1000, null=True, blank=True)
    linkden = models.CharField(max_length=1000, null=True, blank=True)
    reddit = models.CharField(max_length=1000, null=True, blank=True)
    feature_titel = models.CharField(max_length=255, null=True, blank=True)
    feature_1 = models.CharField(max_length=255, null=True, blank=True)
    feature_2 = models.CharField(max_length=255, null=True, blank=True)
    feature_3 = models.CharField(max_length=255, null=True, blank=True)
    feature_4 = models.CharField(max_length=255, null=True, blank=True)
    feature_5 = models.CharField(max_length=255, null=True, blank=True)
    feature_6 = models.CharField(max_length=255, null=True, blank=True)
    logo = models.ImageField(upload_to='media/', null=True, blank=True)
    logo_code = models.CharField(max_length=500000, null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=255)
    cslug = models.SlugField(max_length=255,unique=True, null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Post(models.Model):

    mode1 = (
        ('Online', 'Online'),
        ('Offline', 'Offline'),
    )
    mode2 = (
        ('Offline', 'Offline'),
        ('Online', 'Online'),
    )

    author = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255,unique=True, null=True, blank=True)
    board_name = models.CharField(max_length=255)
    board_name_short = models.CharField(max_length=255)
    post_name = models.CharField(max_length=255) 
    application_mode = models.CharField(choices=mode1, max_length=255, default=True)
    exam_mode = models.CharField(choices=mode2, max_length=255, default=True)
    web_url = models.CharField(max_length=255)
    form_starting_date = models.CharField(max_length=255, null=True, blank=True)
    form_last_date = models.CharField(max_length=255, null=True, blank=True)
    fee_last_date = models.CharField(max_length=255, null=True, blank=True)
    eligibility_criteria = models.CharField(max_length=255, null=True, blank=True)
    year = models.IntegerField(null=True, blank=True)
    age_limit_minimum = models.IntegerField(null=True, blank=True)
    age_limit_maximum = models.IntegerField(null=True, blank=True)
    number_of_post = models.IntegerField(null=True, blank=True)
    general_post = models.IntegerField(null=True, blank=True)
    ewc_post = models.IntegerField(null=True, blank=True)
    ebc_post = models.IntegerField(null=True, blank=True)
    obc_post = models.IntegerField(null=True, blank=True)
    sc_post = models.IntegerField(null=True, blank=True)
    st_post = models.IntegerField(null=True, blank=True)
    creamylayer_post = models.IntegerField(null=True, blank=True)
    general_post_application_fees = models.IntegerField(null=True, blank=True)
    ewc_post_application_fees = models.IntegerField(null=True, blank=True)
    ebc_post_application_fees = models.IntegerField(null=True, blank=True)
    obc_post_application_fees = models.IntegerField(null=True, blank=True)
    sc_post_application_fees = models.IntegerField(null=True, blank=True)
    st_post_application_fees = models.IntegerField(null=True, blank=True)
    creamylayer_fees = models.IntegerField(null=True, blank=True)
    correction_fees = models.IntegerField(null=True, blank=True)
    exam_date = models.CharField(max_length=255, null=True, blank=True)
    latest_jobs = models.CharField(max_length=2000, null=True, blank=True)
    syllabus = models.CharField(max_length=2000, null=True, blank=True)
    previous_year_question_papers = models.CharField(max_length=2000, null=True, blank=True)
    admit_card = models.CharField(max_length=2000, null=True, blank=True)
    admit_card_date = models.CharField(max_length=255, default='Announced Soon')
    answer_key = models.CharField(max_length=2000, null=True, blank=True)
    answer_key_date = models.CharField(max_length=255, default='Announced Soon')
    result = models.CharField(max_length=2000, null=True, blank=True)
    result_date = models.CharField(max_length=255, default='Announced Soon')
    cut_off_marks = models.CharField(max_length=2000, null=True, blank=True)
    cut_off_marks_date = models.CharField(max_length=255, default='Announced Soon')
    photo = models.ImageField(upload_to='media/post/%Y/%m/%d')
    created_date = models.DateTimeField(auto_now_add=True)
    created_date_only = models.DateField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    modified_date_only = models.DateField(auto_now=True)


from django.db.models.signals import pre_save
from django.dispatch.dispatcher import receiver
from .make_slug import unique_slug_generator
@receiver(pre_save, sender=Post)
def pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

    def __str__(self):
        return self.name + ' | '+ str(self.author)
    
