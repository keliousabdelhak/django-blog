from django.urls import path
from . import views

urlpatterns = [
    path('article',views.afficher, name="article"),
    path('commentaire/<int:id>',views.ajouterCommentaire, name="commentaire"),
]
