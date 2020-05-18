from django import forms

from accounts.models import User

class UserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = [
            'first_name', 'username', 'email',
            'phone', 'birth_date', 'sex', 'cpf',
            'zipcode', 'street', 'number', 'complement',
            'district', 'city', 'state'
        ]

    def __init__(self,*args,**kwargs):
        super(UserForm,self).__init__(*args,**kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs={ 'class': 'form-group' }

class EmployeeForm(forms.ModelForm):

    password1 = forms.CharField(label="Senha", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirmação de senha", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = [
            'first_name', 'username', 'email', 'sex', 'cpf'
        ]

    def __init__(self,*args,**kwargs):
        super(EmployeeForm,self).__init__(*args,**kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs={ 'class': 'form-group' }

    def save(self, commit=True):
        user = super(EmployeeForm,self).save(commit=False)
        user.user_type = 'F'
        user.is_active = True
        user.is_staff = True    
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user