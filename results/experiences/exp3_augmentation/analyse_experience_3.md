
### 6.17 Analyse de l'expérience 3 — Data Augmentation

#### Objectif

Nous avons étudié l'effet de petites transformations
aléatoires des images sur l'apprentissage de notre CNN.

Les transformations utilisées sont la rotation,
la translation et le zoom.

#### Résultats obtenus

| Indicateur | Sans augmentation | Avec augmentation |
|---|---:|---:|
| Meilleure époque | 14 | 14 |
| Accuracy validation | 99.27 % | 98.95 % |
| Loss validation | 0.0425 | 0.0404 |
| Durée | 125.9 s | 146.7 s |

#### Comparaison

La différence d'accuracy avec augmentation moins
sans augmentation est de **-0.32 point(s)**.

Le CNN avec augmentation obtient une perte de validation plus faible dans cette expérience.

#### Discussion

L'augmentation des données expose le CNN à de légères
variations visuelles pendant l'entraînement.

Elle peut aider le réseau à mieux généraliser face aux
variations de position, d'orientation et de taille.

Cependant, cette expérience ne permet pas à elle seule
de confirmer une meilleure robustesse sur de nouvelles
conditions d'acquisition.

Une évaluation indépendante reste nécessaire.

#### Conclusion

Cette troisième expérience complète notre étude
des hyperparamètres et des techniques d'amélioration
du CNN.

Nous allons maintenant comparer les trois expériences
afin de sélectionner un modèle final à partir des
performances de validation.
