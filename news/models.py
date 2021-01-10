from django.db import models

from datetime import datetime


class Article(models.Model):
	article_title = models.CharField("Title", max_length = 150)
	announcement = models.CharField("Announcement", max_length = 250)
	article_content = models.TextField('Article content')
	# pub_date = models.DateTimeField('Publication date', default = datetime.now().strftime("%Y-%m-%d %X"))
	pub_date = models.DateTimeField("Publication date", auto_now_add = True)

	def __str__(self):
		return f'{self.article_title} ({self.id})'

	def get_absolute_url(self):
		return f"/news/{self.id}"

	class Meta:
		verbose_name = "Article"
		verbose_name_plural = "Articles"