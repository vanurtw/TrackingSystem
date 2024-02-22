from django import forms
from .models import Tehnique


class TransportTechniqueForm(forms.Form):

    def __init__(self, *args, **kwargs):
        user = args[0].user
        self.base_fields['tec'] = forms.ModelChoiceField(queryset=Tehnique.objects.filter(building=user.building))
        super(TransportTechniqueForm, self).__init__()

    class Meta:
        fields = ['tec']
