from django import forms
from .models import Tehnique
from system_track.models import Building


class TransportTechniqueForm(forms.Form):

    def __init__(self, *args, **kwargs):
        user = args[0].user
        self.base_fields['technique'] = forms.ModelChoiceField(label='Техника',
                                                               queryset=Tehnique.objects.filter(building=user.building,                                                                               status='A'))
        self.base_fields['technique'].widget.attrs = {'class': 'form-control'}
        self.base_fields['buildinq'] = forms.ModelChoiceField(label='Здание куда передать',
                                                               queryset=Building.objects.exclude(name=user.building))
        self.base_fields['buildinq'].widget.attrs = {'class': 'form-control'}
        super(TransportTechniqueForm, self).__init__()

    class Meta:
        fields = ['technique', 'buildinqs']


class StatusUpdateForm(forms.Form):
    CHOICES = [
        ("B", "Техника передана из здания в здание, и ожидает фактического приема"),
        ("C", "Техника принята в здании")
    ]
    status = forms.ChoiceField(label='Статус', choices=CHOICES, widget=forms.Select(attrs={'class':'form-control'}))
    # def __init__(self, *args, **kwargs):
    #     self.base_fields['status'].widget.attrs = {'class':'form-control'}
    #     self.base_fields['status'].initial = 'B'
    #     super(StatusUpdateForm, self).__init__(*args, **kwargs)
    class Meta:
        fields = ['status']
