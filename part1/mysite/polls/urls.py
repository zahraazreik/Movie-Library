from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    #ex: /polls/
    #it was like this: path('',views.index, name='index')
    path('', views.IndexView.as_view(), name='index'),
    
    #ex: /polls/5
    # before: path('<int:question_id>/', views.detail, name = 'detail' )
    # question_id: is the second parameter
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]