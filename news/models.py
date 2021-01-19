from django.db import models
from django.urls import reverse

# from datetime import datetime


class Article(models.Model):
	article_title = models.CharField("Title", max_length = 150)
	announcement = models.CharField("Announcement", max_length = 250)
	article_content = models.TextField('Article content')
	# pub_date = models.DateTimeField('Publication date', default = datetime.now().strftime("%Y-%m-%d %X"))
	pub_date = models.DateTimeField("Publication date", auto_now_add = True)

	def __str__(self):
		return f'{self.article_title} ({self.id})'

	def get_absolute_url(self):
		return reverse("news-detail", kwargs = {"id": self.id})
		# return f"/news/{self.id}" - is a bad method, because when root url /news/ would change,
		# then the get_absolute_url function wouldn't work

	class Meta:
		verbose_name = "Article"
		verbose_name_plural = "Articles"


class Comment(models.Model):
	article = models.ForeignKey(Article, on_delete = models.CASCADE)
	author = models.CharField("Author", max_length = 200)
	comment_content = models.TextField("Comment")
	comment_date = models.DateTimeField("Comment date", auto_now_add = True)

	def __str__(self):
		return self.author

	class Meta:
		verbose_name = "Comment"
		verbose_name_plural = "Comments"