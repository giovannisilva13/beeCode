from django import forms

from products.models import Product

class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'
        exclude = ['quantity']

    def __init__(self,*args,**kwargs):
        super(ProductForm,self).__init__(*args,**kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs={ 'class': 'form-group' }


class ProductExitEntryForm(forms.ModelForm):


    class Meta:
        model = Product
        fields = ['stock_entry', 'stock_exit']

    def __init__(self,*args,**kwargs):
        super(ProductExitEntryForm,self).__init__(*args,**kwargs)
        self.fields['stock_entry'].initial = 50
        self.fields['stock_exit'].initial = 40
        self.fields['stock_entry'].widget.attrs={ 'class': 'form-group' }
        self.fields['stock_exit'].widget.attrs={ 'class': 'form-group'}