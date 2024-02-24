from django.shortcuts import render
from django.views.generic import ListView, View, DetailView
from .models import Tehnique
from .forms import TransportTechniqueForm
from django.db.models import Q


# Create your views here.


class TehniqueViewList(ListView):
    template_name = 'tehnique/tehnique_list.html'
    context_object_name = 'techniques'

    def get_queryset(self):
        user = self.request.user
        search = self.request.GET.get('search', None)
        if search:
            queryset = Tehnique.objects.filter(Q(building=user.building),
                                               Q(name__icontains=search) | Q(inventory_number__icontains=search))
        else:
            queryset = Tehnique.objects.filter(building=user.building, status='A')
        return queryset

    extra_context = {'header': 'technique'}


class TechniqueDetailView(DetailView):
    template_name = 'tehnique/tehnique_detail.html'
    slug_url_kwarg = 'pk'
    context_object_name = 'technique'
    model = Tehnique
    extra_context = {'header': 'technique'}

    def get_context_data(self, **kwargs):
        context = super(TechniqueDetailView, self).get_context_data(**kwargs)
        update = self.request.GET.get('update')
        if update:
            context['update'] = True
        return context



def tehnique_transport(request):
    form = TransportTechniqueForm(request)
    # form.set_tec(request)
    return render(request, 'tehnique/hand_over.html', {'header': 'hand_over', 'form': form})
