# Créez GrandPy Bot, le papy-robot

## <a name="tests"></a>Tests

### <a name="definition"></a>Définition

Définition des tests unitaires (fournie dans la documentation Flask) :
> L'écriture de tests unitaires pour votre application vous permet de vérifier que le code que vous avez écrit fonctionne comme vous le souhaitez. Flask fournit un client de test qui simule les demandes adressées à l'application et renvoir les données de la réponse.  
> Vous devez tester autant de code que possible. Le code dans les fonctions ne s'exécute que lorsque la fonction est appelée, et le code dans les branches, comme les blocs "if", ne s'exécute que lorsque la condition est remplie. Le but est de s'assurer que chaque fonction est bien testée avec des données qui couvrent chaque branche.  
> Plus vous vous rapprocher d'un taux de 100% de couverture, plus vous serez convaincu qu'apporter un changement ne changera pas de manière inattendue un autre comportement. Cependant, un taux de couverture à 100% ne garantit pas que votre application ne comporte pas de bugs. En particulier, il ne teste pas la manière dans l'utilisateur interagit avec l'application dans le navigateur. Malgré cela, la couverture des tests est un outil important à utiliser pendant le développement.

### <a name="installation"></a>Installation

Les packages pytest et coverage nécessaires aux tests de l'application sont inclus dans le fichier <a name="requirements" href="../requirements.txt">requirements.txt</a>.
Pour les installer séparement, vous pouvez effectuer la ligne de commande suivante :  
`$ pip install pytest coverage`  

Les scripts de tests sont inclus dans le dossier <a name="test" href="./">test/</a>.

### <a name="lancer_tests"></a>Lancer les tests

* Pour lancer les tests, utiliser la commande **pytest** :  
`$ pytest`  

Si un test ne passe pas, pytest montrera l'erreur levée.

* Pour mesurer le taux de couverture des tests de l'application, utiliser la commande **coverage** :  
`$ coverage run -m pytest`  

* Deux types de vues du résultats du rapport de couverture sont possibles :
    * En console :  
    `$ coverage report`  
    * Dans un fichier HTML mettant en lumière chaque partie du code couvert par les tests :  
    `$ coverage html`  
    Les fichiers seront générés dans un repertoire `htmlcov/`. Ouvrir le fichier `htmlcov/index.html` dans le navigateur pour voir le rapport édité.
