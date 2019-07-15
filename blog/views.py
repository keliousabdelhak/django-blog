from django.http import HttpResponse
from django.shortcuts import render
from blog.models import Article,Categorie,Commentaire
from .forms import CommentaireForm
from django.shortcuts import redirect
# Create your views here.
def home(request):
    return HttpResponse("<h1>Bienvenue sur mon blog !</h1>")

def afficher(request):
    return render(
        request,
        'blog/voir.html',
        {
            'article':Article.objects.all(),
            'categorie':Categorie.objects.all(),
            'commentaire':Commentaire.objects.all()
        }
    )
def accueil(request):
    return render(request, 'blog/accueil.html')

def ajouterCommentaire(request, id):
    form = CommentaireForm(request.POST or None)
    varz = False
    if form.is_valid():
        
        pseudo = form.cleaned_data['pseudo']
        email = form.cleaned_data['email']
        contenu = form.cleaned_data['contenu']
        envoi = True
        form.save()
        varz = True
    if varz== True:
        return redirect(afficher)
    else:
        print("ça marche")
        return render(request,'blog/commentaire.html',locals(),
        {
            'article':Article.objects.all(),
            'categorie':Categorie.objects.all(),
        })

