from django.shortcuts import render
from django.views.generic import ListView, View
from .models import Tehnique


# Create your views here.


class TehniqueViewList(ListView):
    template_name = 'tehnique/tehnique_list.html'
    model = Tehnique
    extra_context = {'header': 'technique'}


def tehnique_detail(request):
    return render(request, 'tehnique/tehnique_detail.html', {'header': 'technique'})


def tehnique_transport(request):
    return render(request, 'tehnique/transport-tehnique.html', {'header': 'transfer'})
