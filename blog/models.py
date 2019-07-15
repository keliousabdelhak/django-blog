from django.db import models
from django.utils import timezone

#Les articles: 
class Article(models.Model):
    titre = models.CharField(max_length=100) # Ne pas être vide 
    auteur = models.CharField(max_length=42) # Ne pas être vide
    contenu = models.TextField(null=True)    # Possible qu'il soit vide 
    date = models.DateTimeField(default=timezone.now, verbose_name="Date de parution")
    categorie = models.ForeignKey('Categorie', on_delete=models.CASCADE)

    class Meta:
        verbose_name = "article"
        ordering = ['date']
    
    def __str__(self):
        return self.titre

#les catégories:
class Categorie (models.Model):
    nom = models.CharField(max_length=42)

    def __str__(self):
        return self.nom

#les commentaires 
class Commentaire (models.Model):
    pseudo = models.CharField(max_length=100)
    email = models.EmailField()
    contenu = models.TextField(null=True)
    artilce = models.ForeignKey('Article', null= True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.pseudo