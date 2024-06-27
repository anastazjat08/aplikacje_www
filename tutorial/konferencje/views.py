from django.shortcuts import render, get_object_or_404

# Create your views here.

from .models import Conference, Abstract
from django.utils import timezone
from .forms import AbstractForm

def home(request):
	all_conferences = Conference.objects.all()
	all_abstracts = Abstract.objects.all()
	today = timezone.now().date()
	return render(request, 'konferencje/Konferencje.html', {'all_conferences': all_conferences, 'today':today,
		'all_abstracts':all_abstracts})

def dodaj(request, name):

	if request.method == 'POST':
		form = AbstractForm(request.POST)

		if form.valid():
			conference = Conference.objectc.get(name = name)

			abstract = form.save(commit=False)
			abstract.conference = conference
			abstract.save()

	else:
		form = AbstractForm()


	return render(request, 'konferencje/Dodaj.html', {'form':form, 'name':name})

def edytuj(request, name ,title):
	abstract = get_object_or_404(Abstract, title=title)

	if request.method == 'POST':
		form = AbstractForm(request.POST, instance=abstract)

		if form.is_valid():
			form.save()

	else:
		form = AbstractForm(instance=abstract)

	return render(request, 'konferencje/Edytuj.html', {'form':form, 'name':name,'title': title})