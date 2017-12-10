from django import forms
from api.models import Sermon

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Sermon
        fields = ('description', 'document', )