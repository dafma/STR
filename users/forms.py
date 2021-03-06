from django import forms
from .models import User,TIPO_USUARIO





class UserRegisterForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'first_name',)
        widgets={
            'email': forms.TextInput(attrs={'type':'email','id':"email",  'name':"email",'ng-model':"formData.email",'required':'','class': 'form-control form-group ng-pristine ng-invalid ng-invalid-required ng-valid-email', 'placeholder': 'Ingresa tu e-mail',

                                            }),
            'first_name': forms.TextInput(attrs={'type':'text','id':'name' ,'name':'name','required':'', 'class':'form-control form-group ng-pristine ng-invalid ng-invalid-required '}),
            'username': forms.TextInput(attrs={'type':'text','id':"username",'ng-model':'formData.name','ng-minlength':'5','ng-maxlength':'20','ng-pattern':'/^[A-z][A-z0-9]*$/','required':'','class': 'form-group form-control ng-pristine ng-invalid ng-invalid-required ng-valid-maxlength ng-valid-minlength ng-valid-pattern'}),
            'password': forms.TextInput(attrs={'type':'password','id':"password",'name':"password",'ng-model':"formData.password",'ng-minlength':'8', 'ng-maxlength':'20','ng-pattern':'/(?=.*[a-z])(?=.*[A-Z])(?=.*[^a-zA-Z])/','required':'','class':'form-control form-group ng-pristine ng-invalid ng-invalid-required ng-valid-maxlength ng-valid-minlength ng-valid-pattern',
                                               'required':'true','minlength':"8",'maxlength':"20",

                                               'ng-pattern':"/(?=.*[a-z])(?=.*[A-Z])(?=.*[^a-zA-Z])/"}),

        }
    #comnpruba que el nombre de usuario no exista
    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username):
            raise forms.ValidationError('el nombre de usuario ya existe')
        return

    def clean_email(self):
        #comprueba que n o existe un email
        email = self.cleaned_data['email']
        if User.objects.filter(email=email):
            raise forms.ValidationError("ya existe un email parecido a este.")
        return email



class LoginForm(forms.Form):
    username = forms.CharField(max_length=30,widget= forms.TextInput(attrs={'class': 'form-control', 'placeholder':'ingresa tu usuario','required':'true'}))
    password = forms.CharField(max_length=30,widget= forms.TextInput(attrs={'type':'password',
                                                                            'class':'form-control',
                                                                            'placeholder':'ingresa tu password','required':'true'}))


