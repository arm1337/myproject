from django.shortcuts import render, redirect
from .forms import RegisterForm


def register_index(request):
	if request.method == "POST":
		form = RegisterForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect("home")
	else:
		form = RegisterForm()

	data = {
		"form": form,
	}
	return render (request, "register/register_index.html", data)