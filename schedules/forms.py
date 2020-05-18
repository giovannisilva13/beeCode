from django import forms

from schedules.models import Schedule

class ScheduleForm(forms.ModelForm):

    class Meta:
        model = Schedule
        fields = '__all__'
        exclude = [ 'status', ]

    def __init__(self,*args,**kwargs):
        super(ScheduleForm,self).__init__(*args,**kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs={ 'class': 'form-control' }