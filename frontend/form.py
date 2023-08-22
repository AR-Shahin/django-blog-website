from django import forms
from .models import *

class ContactUsForm(forms.ModelForm):

    
    class Meta:
        model = Contact
        fields = ['name', 'email',"subject","message"]
        
    name = forms.CharField(
        label='Name',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Name',"name":"name" ,"id":"name"}),
        required=False
    )
    
    email = forms.CharField(
        label='Email',
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Your Email',"name":"email" ,"id":"email","type" : "email",}),
        required=False  
    )
    
    subject = forms.CharField(
        label='Subject',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Subject',"name":"subject" ,"id":"subject","type" : "text",}),
        required=False  
    )
    
    
    message = forms.CharField(
        label='Message',
        widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Message',"name":"message" ,"id":"message","rows":"5"}),
        required=False  
    )