from django import forms
from .models import Comment  # Asumiendo que el modelo de comentarios está en la misma app

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['review']

