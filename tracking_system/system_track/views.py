from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView
from tehnique.models import Tehnique
from django.http import HttpResponse
from mimesis import Payment


# Create your views here.


class HomeView(TemplateView):
    template_name = 'system_track/index.html'


def track_technique(request):
    return render(request, 'system_track/transferred-equipment.html', {'header': 'track'})


def hand_over_technique(request):
    paytment = Payment()
    technique_id = request.POST.get('technique')
    building_id = request.POST.get('buildinq')
    tehnique = get_object_or_404(Tehnique, id=technique_id)
    tehnique.building_id = building_id
    tehnique.parent_building = request.user.building
    tehnique.status = 'B'
    while True:
        try:
            tehnique.inventory_number = paytment.credit_card_number()
            break
        except:
            continue
    tehnique.save()
    return HttpResponse('aa')
