from django import forms
from .models import Tehnique
from system_track.models import Building


class TransportTechniqueForm(forms.Form):

    def __init__(self, *args, **kwargs):
        user = args[0].user
        self.base_fields['technique'] = forms.ModelChoiceField(label='Техника',
                                                               queryset=Tehnique.objects.filter(building=user.building,
                                                                                                status='A'))
        self.base_fields['technique'].widget.attrs = {'class': 'form-control'}
        self.base_fields['buildinq'] = forms.ModelChoiceField(label='Здание куда передать',
                                                               queryset=Building.objects.exclude(name=user.building))
        self.base_fields['buildinq'].widget.attrs = {'class': 'form-control'}
        super(TransportTechniqueForm, self).__init__()

    class Meta:
        fields = ['technique', 'buildinqs']
