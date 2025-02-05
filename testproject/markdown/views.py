from django.forms import modelformset_factory
from django.shortcuts import render

from .models import Markdown


# Create your views here.
def index(request, template="markdown/index.html"):
    formset = modelformset_factory(Markdown, fields=("title", "content"))
    return render(request, template, {"formset": formset})
