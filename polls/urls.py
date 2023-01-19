from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:question_id>/', views.get_question, name='get_question'),
    path('<int:question_id>/result/', views.get_result, name='get_result'),
    path('<int:question_id>/vote/', views.submit_result, name='submit_result')
]
