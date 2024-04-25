
from django.contrib import admin
from django.urls import path
from . import views 

app_name = "qapp"
urlpatterns = [
    path('', views.home, name='home'),
    path('first_run', views.first_run, name='first_run'),
    path('save_factoid_questions', views.save_factoid_questions, name='save_factoid_questions'),
    path('create_dataset', views.create_dataset, name='create_dataset'),
    path('save_nonfactoid_questions', views.save_nonfactoid_questions, name='save_nonfactoid_questions'),
    path('save_factoid_done', views.save_factoid_done, name='save_factoid_done'),
    path('temp_dataset', views.temp_dataset, name='temp_dataset'),
    path('save_automatic_questions', views.save_automatic_questions, name='save_automatic_questions'),
    path('delete_bad_questions', views.delete_bad_questions, name='delete_bad_questions'),
    path('save_multiple_automatic', views.save_multiple_automatic, name='save_multiple_automatic'),
    path('mt5_questions', views.mt5_questions, name='mt5_questions'),
    path('save_quqa_done', views.save_quqa_done, name='save_quqa_done'),
    path('save_quqa', views.save_quqa, name='save_quqa'),
    path('save_qaraatiFirst', views.save_qaraatiFirst, name='save_qaraatiFirst'),
    path('save_qaraatiSecond', views.save_qaraatiSecond, name='save_qaraatiSecond'),
    path('save_qaraatiThird', views.save_qaraatiThird, name='save_qaraatiThird'),
    path('save_rule_based', views.save_rule_based, name='save_rule_based'),
    # path('delete_everything', views.delete_everything, name='delete_everything'),
]
