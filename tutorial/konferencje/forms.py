from django.forms import ModelForm
from .models import Abstract

class AbstractForm(ModelForm):
	class Meta:
		model = Abstract
		fields = ["title","text", "type_a","author", "affiliation"]