from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse
from django.shortcuts import render
from task.forms import PeselForm
from task.services.pesel_corectness_checker import PeselValidator


# Create your views here.
def home(request: WSGIRequest) -> HttpResponse:
    form = PeselForm
    context = {"form": form}
    if request.method == "POST":
        form = PeselForm(request.POST)
        if form.is_valid():
            pesel = request.POST["pesel"]
            validator = PeselValidator(pesel)
            context = {
                "result": validator.is_valid(),
                "pesel": pesel,
                "text": validator.message,
            }
            return render(request, "result.html", context)
    return render(request, "pesel_form.html", context)
