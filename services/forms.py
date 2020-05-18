from django import forms

from services.models import Service

class ServiceForm(forms.ModelForm):

    class Meta:
        model = Service
        fields = '__all__'

    def __init__(self,*args,**kwargs):
        super(ServiceForm,self).__init__(*args,**kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs={ 'class': 'form-group' }