from django.shortcuts import render, redirect
from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse

from .forms import PeselForm

from .utils import check_pesel


# Create your views here.
def home(request: WSGIRequest) -> HttpResponse:
    form = PeselForm
    context = {"form": form}
    if request.method == "POST":
        form = PeselForm(request.POST, request.FILES)
        if form.is_valid():
            pesel = request.POST["pesel"]
            result, text = check_pesel(pesel)
            context = {"result": result, "pesel": pesel, "text": text}
            return render(request, "result.html", context)
    return render(request, "pesel_form.html", context)
