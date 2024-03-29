from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, TemplateView
from tehnique.models import Tehnique
from django.db.models import Q
from django.http import HttpResponse
from mimesis import Payment


# Create your views here.


class HomeView(TemplateView):
    template_name = 'system_track/index.html'


class TrackView(ListView):
    context_object_name = 'techniques_transport'
    template_name = 'system_track/track.html'
    extra_context = {'header': 'track'}

    def get_queryset(self):
        request = self.request
        building_user = request.user.building
        queryset = Tehnique.objects.exclude(building=building_user).filter(parent_building=building_user,
                                                                           status='B')
        search = request.GET.get('search', None)
        if search:
            queryset = queryset.filter(Q(name__icontains=search)|Q(inventory_number__icontains=search))
        return queryset.order_by('-date_update')


class AcceptView(ListView):
    template_name = 'system_track/accept.html'
    context_object_name = 'technique_accept'
    extra_context = {'header': 'accept'}

    def get_queryset(self):
        building_user = self.request.user.building
        queryset = Tehnique.objects.filter(building=building_user, status='B')
        search = self.request.GET.get('search')
        if search:
            queryset = queryset.filter(Q(name__icontains=search) | Q(inventory_number__icontains=search))
        return queryset.order_by('-date_update')


def hand_over_technique(request):
    technique_id = request.POST.get('technique')
    building_id = request.POST.get('buildinq')
    tehnique = get_object_or_404(Tehnique, id=technique_id)
    tehnique.building_id = building_id
    tehnique.parent_building = request.user.building
    tehnique.status = 'B'
    tehnique.save()
    return redirect('track')
