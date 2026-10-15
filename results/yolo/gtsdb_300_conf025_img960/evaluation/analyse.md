
### 11.7 Analyse et interprétation des résultats

Nous avons évalué notre détecteur YOLO sur **300 scènes routières GTSDB**.

Le fichier officiel contient **476 annotations de panneaux**
pour ces scènes. Notre détecteur a produit **832 détections**.

#### Évaluation de la localisation

| Indicateur | Résultat |
|---|---:|
| Vrais positifs | 1 |
| Faux positifs | 831 |
| Faux négatifs | 475 |
| Précision | 0.12% |
| Rappel | 0.21% |
| F1-score | 0.15% |

Une localisation est considérée correcte lorsque son IoU est
supérieur ou égal à **0.5**.

#### Évaluation de la classification

Parmi les **1 détections correctement localisées**,
notre CNN a reconnu correctement **0 catégories**.

L'accuracy de classification sur ces détections est de
**0.00%**.

#### Performance du système complet

Le rappel de bout en bout YOLO + CNN est de **0.00%**.

Cette métrique indique la proportion des panneaux annotés
qui sont à la fois correctement localisés et correctement classifiés.

#### Limites de l'évaluation

Les résultats dépendent du seuil de détection YOLO fixé à 0.25,
du seuil IoU fixé à 0.5, du modèle utilisé et des données GTSDB.

La correspondance entre détections et annotations est effectuée
en privilégiant les paires ayant les IoU les plus élevés,
sans réutiliser deux fois la même annotation.

Les résultats ne permettent pas de garantir des performances
identiques sur toutes les scènes routières.
