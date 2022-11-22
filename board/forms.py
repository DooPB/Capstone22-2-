from django import forms
from .models import CoinBoard

class BoardAdd(forms.ModelForm):
    class Meta:
        model = CoinBoard
        fields = ('board_title', 'content')
        exclude = ('write_user',)
        labels = {
            'board_title':'제목을 입력하세요.',
            'content':'내용을 입력하세요.',
        }