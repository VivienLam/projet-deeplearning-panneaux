
### 6.12 Analyse de l'expérience 2 — Dropout

#### Objectif

Nous avons étudié l'influence d'une couche Dropout(0.3)
placée après la couche Dense de 128 neurones.

Les deux CNN ont été entraînés avec les mêmes principaux
hyperparamètres et les mêmes poids initiaux.

#### Résultats obtenus

| Indicateur | Sans Dropout | Avec Dropout |
|---|---:|---:|
| Meilleure époque | 14 | 15 |
| Accuracy validation | 99.27 % | 99.35 % |
| Loss validation | 0.0425 | 0.0344 |

#### Comparaison

La différence d'accuracy avec Dropout moins sans Dropout
est de **+0.08 point(s)**.

L'ajout du Dropout a permis d'obtenir une perte de validation plus faible dans cette expérience.

#### Discussion

Le Dropout peut contribuer à limiter le surapprentissage
en désactivant aléatoirement certaines activations pendant
l'entraînement.

Cependant, son efficacité dépend du modèle, du taux
choisi et des données.

Cette expérience repose sur une seule exécution
pour chaque configuration. Les résultats ne permettent
donc pas de conclure à une supériorité systématique.

#### Conclusion

Cette expérience permet d'observer l'effet du Dropout
sur notre CNN GTSRB, dans les conditions retenues.

Nous poursuivrons avec une troisième expérience consacrée
à l'augmentation des données.
