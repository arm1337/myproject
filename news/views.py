from django.shortcuts import render, redirect, reverse
from django.http import Http404, HttpResponseRedirect
from django.views.generic import DetailView, UpdateView, DeleteView   # ListView

from .models import Article, Comment
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

	return render(request, 'news/create.html', data)

def leave_comment(request, article_id):
	try:
		a = Article.objects.get( id = article_id )
	except:
		raise Http404("Article does not exist!")

	a.comment_set.create(author = request.POST['author_name'], comment_content = request.POST['comment_content'])

	return HttpResponseRedirect( reverse( "news:news-detail", args = [ a.id, ] ) )