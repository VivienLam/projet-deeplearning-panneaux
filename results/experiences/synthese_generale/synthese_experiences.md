
### 6.20 Synthèse des expérimentations

#### Résultats comparatifs

| Configuration | Accuracy validation | Val loss |
|---|---:|---:|
| Avec Dropout | 99.35 % | 0.0344 |
| Avec augmentation | 98.95 % | 0.0404 |
| Sans Dropout | 99.27 % | 0.0425 |
| Sans augmentation | 99.27 % | 0.0425 |
| CNN initial | 99.25 % | 0.0450 |
| LR 0.001 | 99.03 % | 0.0592 |
| LR 0.0005 | 98.71 % | 0.0643 |

#### Sélection du modèle

Le modèle ayant obtenu la plus faible perte de
validation dans les expériences présentées est :

**Avec Dropout**

Ses performances de validation sont :

- Accuracy : **99.35 %**
- Val loss : **0.0344**
- Meilleure époque : **15**

Ce modèle est retenu comme candidat pour
l'évaluation finale sur le jeu de test officiel.

#### Limites

Cette sélection repose sur les résultats observés
sur un unique découpage entraînement/validation.

Les configurations n'ont pas toutes été répétées
avec plusieurs graines aléatoires.

Les résultats du jeu de test permettront d'estimer
la capacité de généralisation du modèle sélectionné,
sans servir à modifier à nouveau ses hyperparamètres.
