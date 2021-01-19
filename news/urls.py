from django.urls import path

from . import views


app_name = "news"
urlpatterns = [
	path('', views.news_home, name='news_home'),
	path('create/', views.create, name="create"),
	path('<int:pk>/', views.NewsDetailView.as_view(), name="news-detail"),
	path('<int:article_id>/leave_comment', views.leave_comment, name="leave_comment"),
	path('<int:pk>/update', views.NewsUpdateView.as_view(), name="news-update"),
	path('<int:pk>/delete', views.NewsDeleteView.as_view(), name="news-delete"),
]