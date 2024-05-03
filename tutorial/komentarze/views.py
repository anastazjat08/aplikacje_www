import datetime
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from django.utils import timezone
from .models import Comment
from .forms import CommentForm
from django.contrib import messages


# Create your views here.
def thanks(request, author_name):
	return render(request, 'komentarze/thanks.html', {'author_name':author_name})

def thanks_message(request, author_name, message):
	return render(request, 'komentarze/thanks.html', {'author_name':author_name, 'message':message})

def create_comment(request):
	#comment = get_object_or_404(Comment, pk=pk)

	if request.method == 'POST':
		#tworzenie obiektu forms i zapełnienie obiektu danymi
		form = CommentForm(request.POST)

		if form.is_valid():
			#stwórz obiekt, ale jeszcze nie zapisuj do bazy danych
			#żeby modyfikować
			comment = form.save(commit=False)
			comment.date_creation = timezone.now()
			message=None

			if comment.date_published < timezone.now():
				message = messages.error(request, "Data publikacji jest przeszła.")
				comment.date_published = timezone.now()
				

			comment.save()
			author_name = form.cleaned_data['author']
			if message==None:
				return redirect("komentarze:thanks", author_name=author_name)
			elif message != None:
				return redirect("komentarze:thanks_message", author_name=author_name, message=message)
	else:
		#GET użytkownik otworzył stronę z formularzem, tworzymy nowy
		form = CommentForm()
	return render(request, 'komentarze/create_comment.html', {'form':form})

