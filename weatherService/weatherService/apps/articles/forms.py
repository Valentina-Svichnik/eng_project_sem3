from .models import New
from django.forms import ModelForm, TextInput, widgets, Textarea

class NewsForm(ModelForm):
    class Meta:
        model = New
        fields = ['date', 'subject', 'heading', 'picture', 'description', 'source']

        widgets = {
            'date' : TextInput(attrs={
                'class' : 'form-control',
                'type' : 'date',
                'id' : 'date',
                'placeholder' : '01.01.2021'
            }),
            'subject' : TextInput(attrs={
                'class' : 'form-control',
                'type' : 'text',
                'id' : 'subject',
                'placeholder' : 'Тема'
            }),
            'heading' : TextInput(attrs={
                'class' : 'form-control',
                'type' : 'text',
                'id' : 'heading',
                'placeholder' : 'Заголовок'
            }),
            'picture' : TextInput(attrs={
                'class' : 'form-control',
                'type' : 'text',
                'id' : 'way',
                'value' : '/static/img/...'
            }),
            'description' : Textarea(attrs={
                'class' : 'form-control',
                'type' : 'text',
                'id' : 'description',
                'placeholder' : 'Текст новости'
            }),
            'source' : TextInput(attrs={
                'class' : 'form-control',
                'type' : 'text',
                'id' : 'source',
                'placeholder' : 'Источник'
            }),
            
        }