# Créez GrandPy Bot, le papy-robot


<!-- Lien GitHub vers le projet : [OC_Projet6_Ppizza2_MP](https://github.com/MickaPch/OC_Projet6_Ppizza2_MP) -->


OpenClassrooms - Projet n°7 - Parcours *Développeur d'applications - Python*  
Auteur : [MickaP](https://github.com/MickaPch/)  


> Ah, les grands-pères... Je ne sais pas vous, mais le mien connaissait quantité d'histoires. Il me suffisait de lui dire un mot pour le voir partir pendant des heures. "Tu veux l'adresse de la poste ? Ah oui, c'est bien. Mais je t'ai déjà raconté que j'ai aidé à la construire ? C'était en 1974 et..."

> Pourtant, j'adore ses récits ! J'ai beaucoup appris et rêvé d'autres contrées en l'écoutant. Voici donc le projet proposé : créer un robot qui vous répondrait comme votre grand-père ! Si vous lui demandez l'adresse d'un lieu, il vous la donnera, certes, mais agrémentée d'un long récit très intéressant. Vous êtes prêt ?


## Sommaire
* [Cahier des charges](#cahier_des_charges)
    * [Fonctionnalités](#fonctionnalites)
    * [Parcours utilisateur](#parcours_utilisateur)


## <a name="cahier_des_charges"></a>Cahier des charges


### <a name="fonctionnalites"></a>Fonctionnalités


* Interactions en AJAX : l'utilisateur envoie sa question en appuyant sur entrée et la réponse s'affiche directement dans l'écran, sans recharger la page.
* Vous utiliserez l'API de Google Maps et celle de Media Wiki
* Rien n'est sauvegardé. Si l'utilisateur charge de nouveau la page, tout l'historique est perdu.
* Vous pouvez vous amuser à inventer plusieurs réponses différentes de la part de GrandPy mais ce n'est pas une obligation. Amusez-vous !


### <a name="parcours_utilisateur"></a>Parcours utilisateur


L'utilisateur ouvre son navigateur et entre l'URL que vous lui avez fournie. Il arrive devant une page contenant les éléments suivants :
* header : logo et phrase d'accroche
* zone centrale : zone vide (qui servira à afficher le dialogue) et champ de formulaire pour envoyer une question
* footer : votre prénom & nom, lien vers votre repository GitHub et autres réseaux sociaux si vous en avez

L'utilisateur tape "Salut GrandPy ! Est-ce que tu connais l'adresse d'OpenClassrooms ?" dans le champ de formulaire puis appuie sur la touche Entrée. Le message s'affiche dans la zone du dessus qui affiche tous les messages échangés. Une icône tourne pour indiquer que GrandPy est en train de réfléchir.

Puis un nouveau message apparaît : "Bien sûr mon poussin ! La voici : 7 cité du Paradis, 75010 Paris." En-dessous, une carte Google Maps apparaît également avec un marqueur indiquant l'adresse demandée.

GrandPy envoie un nouveau message : "Mais t'ai-je déjà raconté l'histoire de ce quartier qui m'a vu en culottes courtes ? La cité Paradis est une voie publique située dans le 10e arrondissement de Paris. Elle est en forme de té, une branche débouche au 43 rue de Paradis, la deuxième au 57 rue d'Hauteville et la troisième en impasse.
[[En savoir plus sur Wikipedia](https://fr.wikipedia.org/wiki/Cit%C3%A9_Paradis)]"

