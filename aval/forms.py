from django import forms
from .models import Avaliation

class AvaliationForm(forms.ModelForm):
    class Meta:
        model = Avaliation

        fields = ['tee', 'pro', 'lid', 'fle', 'ini', 'pon', 'com',
                  'cup', 'pst', 'err', 'org', 'cpi', 'p_pos', 'p_neg']


