from django import forms

class ContactForm(forms.Form):
    first_name = forms.CharField(label='Nombre', required=True, widget=forms.TextInput(
        attrs={'class':'form-control'}
    ), min_length=2, max_length=40)
    
    last_name = forms.CharField(label='Apellido', required=True, widget=forms.TextInput(
        attrs={'class':'form-control'}
    ), min_length=2, max_length=40)
    
    email = forms.EmailField(label='Email', required=True, widget=forms.EmailInput(
        attrs={'class':'form-control'}
    ))
    
    subject = forms.CharField(label='Asunto', required=True, widget=forms.TextInput(
        attrs={'class':'form-control'}
    ), min_length=5, max_length=70)
    
    message = forms.CharField(label='Mensaje', required=True, widget=forms.Textarea(
        attrs={'class':'form-control', 'rows':6}
    ), min_length=10, max_length=1000)
