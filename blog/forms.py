from django import forms

class ContactUsForm(forms.Form):
    name = forms.CharField(
        label='Name',
        max_length=100,
        widget=forms.TextInput(attrs={'placeholder': 'Your Name'}),
    )
    email = forms.EmailField(
        label='Email',
        max_length=100,
        widget=forms.TextInput(attrs={'placeholder': 'Your Email'}),
    )
    subject = forms.CharField(
        label='Subject',
        max_length=100,
        widget=forms.TextInput(attrs={'placeholder': 'Your Subject'}),
    )
    message = forms.CharField(
        label='Message',
        max_length=1000,
        widget=forms.Textarea(attrs={'placeholder': 'Your Message'}),
    )