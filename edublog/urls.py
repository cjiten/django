from django.urls import path
from edublog import views

urlpatterns = [
    path('', views.home, name="home"),
    path('admit-cards', views.admitcard, name="admitcard"),
    path('answer-key', views.answerkey, name="answerkey"),
    path('cut-off-marks', views.cutoffmarks, name="cutoffmarks"),
    path('latest-jobs', views.latestjobs, name="latestjobs"),
    path('result', views.result, name="result"),
    path('syllabus', views.syllabus, name="syllabus"),
    path('previous-year-question-papers', views.pyqp, name="pyqp"),
    path('contact-us', views.contact, name="contact"),
    path('resent-post', views.resentpost, name="resentpost"),
    path('category', views.category, name="category"),
    path('en/<str:slugcat>/<slug:slug>', views.slink, name="slink"),
    path('hi/<str:slugcat>/<slug:slug>', views.shlink, name="shlink"),
    path('search', views.search, name="search"),
    path('sitemap.xml',  views.sitemap, name="sitemap")
]
