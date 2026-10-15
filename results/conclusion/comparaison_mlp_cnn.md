
### 8.4 Résultats et interprétation

Nous avons évalué le MLP et le CNN sur les mêmes
12 630 images du jeu de test officiel GTSRB.

| Indicateur | MLP | CNN |
|---|---:|---:|
| Accuracy | 85.22 % | 95.78 % |
| Précision macro | 82.81 % | 95.42 % |
| Rappel macro | 79.66 % | 93.18 % |
| F1-score macro | 80.12 % | 93.81 % |

#### Analyse

Le CNN obtient une accuracy supérieure à celle du MLP sur le jeu de test étudié.

La différence d'accuracy (CNN - MLP) est de
**+10.56 point(s)**.

Le MLP traite les pixels après aplatissement,
tandis que le CNN exploite des convolutions
pour apprendre des caractéristiques spatiales.

Les résultats observés permettent de comparer
l'efficacité des architectures sur ce jeu de test.

#### Limites

Cette comparaison repose sur deux modèles déjà
entraînés et un unique jeu de test officiel.

Elle ne constitue pas une preuve que l'architecture
obtenant le meilleur score serait supérieure
sur toutes les données ou dans tous les contextes.
