from .models import Films
from django.forms import ModelForm, TextInput, Textarea

class FilmsForm(ModelForm):
    class Meta:
        model = Films
        fields = ['title', 'description', 'feedback', 'imageurl']
        widgets = {
            'title': TextInput(attrs={'class': 'form-control', 'placeholder': 'Заголовок'}),
            'description': TextInput(attrs={'class': 'form-control', 'placeholder': 'Описание'}),
            'feedback': Textarea(attrs={'class': 'form-control', 'placeholder': 'Отзыв'}),
            'imageurl': TextInput(attrs={'class': 'form-control', 'placeholder': 'Картинка'}),

        }