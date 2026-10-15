
### 5.8 Analyse et interprétation des résultats

#### 1. Performances globales du CNN

L'évaluation du meilleur CNN sur les **7842 images
de validation** donne les résultats suivants :

| Indicateur | Valeur |
|---|---:|
| Accuracy | 99.25 % |
| Précision macro | 99.17 % |
| Rappel macro | 99.11 % |
| F1-score macro | 99.14 % |
| Images correctement classées | 7783 |
| Images incorrectement classées | 59 |
| Taux d'erreur | 0.75 % |

Les métriques macro correspondent aux moyennes calculées
sur les 43 classes en leur donnant le même poids.

#### 2. Classes les plus difficiles à reconnaître

Le tableau suivant présente les cinq classes qui ont
obtenu les rappels les plus faibles :

| Classe | Rappel | Images de validation |
|---|---:|---:|
| Cyclistes | 94.44 % | 54 |
| Passage enfants | 96.30 % | 108 |
| Succession de virages | 96.97 % | 66 |
| Limitation 80 km/h | 97.58 % | 372 |
| Limitation 20 km/h | 97.62 % | 42 |

Un faible rappel signifie qu'une proportion importante
des images appartenant réellement à cette classe
n'a pas été correctement reconnue.

Ces résultats doivent être interprétés en tenant compte
du nombre d'exemples disponibles par classe.

#### 3. Principales confusions observées

- **Limitation 30 km/h** confondu avec **Limitation 120 km/h** : 3 image(s).
- **Limitation 80 km/h** confondu avec **Limitation 60 km/h** : 3 image(s).
- **Limitation 60 km/h** confondu avec **Limitation 80 km/h** : 2 image(s).

Ces confusions indiquent quelles catégories sont
le plus souvent prises pour d'autres.

L'examen visuel des images mal classées permettra
de rechercher des explications possibles : formes
semblables, chiffres proches, flou, luminosité ou angle.

#### 4. Limites de cette évaluation

Les résultats présentés concernent uniquement
l'ensemble de validation.

Celui-ci provient d'une séparation aléatoire stratifiée
des images d'entraînement GTSRB.

Des images visuellement proches peuvent éventuellement
se retrouver dans les deux ensembles, ce qui peut rendre
la validation optimiste.

Nous devons donc confirmer les performances du modèle
final sur le jeu de test officiel indépendant.

#### 5. Conclusion

Cette évaluation permet de compléter l'accuracy globale
avec des métriques par classe et une analyse des erreurs.

Les résultats serviront à identifier les principales
faiblesses du CNN et à orienter les expérimentations
de la partie 6.
