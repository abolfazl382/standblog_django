from django import forms
from django.core.validators import ValidationError

from blog.models import Message


class ContactUsForm(forms.Form):

    # birth_year = forms.DateField(widget=forms.SelectDateWidget(years=['1900','2000','2020']))
    # color = forms.ChoiceField(widget=forms.Select(attrs={'class' : 'form-control'}),
    #                           choices=[('red', 'red'),('blue', 'blue')],
    #                           required=False,
    #                           )
    # name = forms.CharField(
    #     label='Name',
    #     max_length=100,
    #     widget=forms.TextInput(attrs={'placeholder': 'Your Name'}),
    # )
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

    def clean(self):
        name = self.cleaned_data.get('name')
        message = self.cleaned_data.get('message')

        # if '*' in name.lower():
        #     self.add_error('name', '"*" cannot be in name')
        #
        # if name == message:
        #     raise ValidationError('Name must be different', code='101')

    # executed befor clean method
    # def clean_name(self):
    #     name = self.cleaned_data.get('name')
    #     if 'a' in name:
    #         raise ValidationError('"a" shouldn`t be in name', code='102')
    #     return name

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['subject', 'body', 'email'] # '__all__'
        # exclude = ('email',)
        widgets = {
            'subject' : forms.TextInput(attrs={'placeholder': 'Your Subject'}),
            'email' : forms.TextInput(attrs={'placeholder': 'Your Email'}),
            'body' : forms.Textarea(attrs={'placeholder': 'Your Message'}),
        }