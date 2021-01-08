from django.shortcuts import render, redirect
from django.http import Http404
from django.views.generic import DetailView, UpdateView, DeleteView   # ListView

from .models import Article
from .forms import ArticleForm


def news_home(request):
	latest_news = Article.objects.order_by('-pub_date')
	return render (request, 'news/news_home.html', {'latest_news': latest_news})

class NewsDetailView(DetailView):
	model = Article
	template_name = "news/detail.html"
	context_object_name = "article"   # key name

class NewsUpdateView(UpdateView):
	model = Article
	template_name = "news/update.html"
	form_class = ArticleForm

class NewsDeleteView(DeleteView):
	model = Article
	success_url = "/news"
	template_name = "news/news_delete.html"


def create(request):
	error = ''
	if request.method == 'POST':
		form = ArticleForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('news_home')
		else:
			error = 'Invalid form!'

	form = ArticleForm()

	data = {
		'form': form,
		'error': error,
	}

	return render (request, 'news/create.html', data)