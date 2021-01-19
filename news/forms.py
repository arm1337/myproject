from django.forms import ModelForm, TextInput, Textarea, DateTimeInput

from .models import Article, Comment


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
		}

# class CommentForm(ModelForm):
# 	model = Comment
# 	fields = ['author', 'comment_content']

# 	widgets = {
# 		'author': TextInput(attrs = {
# 				'placeholder': 'Your name',
# 			}),

# 		'comment_content': Textarea(attrs = {
# 				'placeholder': "Your comment",
# 			}),
# 	}