from django.forms import ModelForm
from .models import Comment

class CommentForm(ModelForm):
	class Meta:
		model = Comment
		fields = ["text", "author", "date_creation", "date_published"]