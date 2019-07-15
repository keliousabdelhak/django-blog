from django import forms 
from .models import Article,Categorie,Commentaire


class CommentaireForm(forms.ModelForm):
    class Meta:
        model = Commentaire
        fields = '__all__'
    