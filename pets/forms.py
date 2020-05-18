from django import forms

from pets.models import Pets

class PetForm(forms.ModelForm):
    
    class Meta:
        model = Pets
        fields = '__all__'

    def __init__(self,*args,**kwargs):
        super(PetForm,self).__init__(*args,**kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs={ 'class': 'form-group' }