from django.forms import ModelForm, TextInput, Textarea, DateTimeInput

from .models import Article


class ArticleForm(ModelForm):
	class Meta:
		model = Article
		fields = ['article_title', 'announcement', 'article_content']

		widgets = {
			'article_title': TextInput(attrs = {
					'class': 'form-control',
					'placeholder': 'Article title',
				}),
			'announcement': TextInput(attrs = {
					'class': 'form-control',
					'placeholder': 'Announcement',
				}),
			'article_content': Textarea(attrs = {
					'class': 'form-control',
					'placeholder': 'Article content',
				}),
			# 'pub_date': DateTimeInput({
			# 		'class': 'form-control',
			# 		'placeholder': 'Publication date',
			# 	}),
		}