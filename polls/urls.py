from django.urls import path
from . import views

urlpatterns = [
 path('', views.index, name='index'),
 path('index2/', views.index2),
 path('logout/', views.logout),
 path('login/', views.login, name='login'),
 path('login_post/', views.login_post),
 path('<int:question_id>/', views.detail, name='detail'),
 path('<int:question_id>/results/', views.results, name='results'),
 path('<int:question_id>/vote/', views.vote, name='vote'),
 path('<int:question_id>/reset/', views.reset, name='reset'),
]