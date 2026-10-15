
### 6.7 Analyse de l'expérience 1

#### Objectif

Nous avons étudié l'influence du learning rate sur
l'entraînement de notre CNN.

Nous avons comparé deux configurations identiques,
avec des learning rates de 0.001 et 0.0005.

Les modèles ont été initialisés avec les mêmes poids.

#### Résultats obtenus

| Indicateur | CNN A | CNN B |
|---|---:|---:|
| Learning rate | 0.001 | 0.0005 |
| Meilleure époque selon val_loss | 15 | 15 |
| Accuracy à cette époque | 99.03 % | 98.71 % |
| Meilleure val_loss | 0.0592 | 0.0643 |

#### Comparaison

La différence d'accuracy entre les configurations
B et A est de **-0.32 point(s)**.

La différence de perte de validation B - A est
de **+0.0052**.

Le learning rate 0.001 obtient une perte de validation plus faible que le learning rate 0.0005 dans cette comparaison.

#### Discussion

Cette expérience permet d'observer l'effet du taux
d'apprentissage dans les conditions étudiées.

Les résultats d'une seule exécution ne suffisent
pas à garantir que la meilleure configuration
restera supérieure avec d'autres initialisations.

Nous conservons les deux modèles et leurs historiques
afin de pouvoir reproduire et approfondir l'expérience.

#### Conclusion

Cette première expérience apporte des informations
sur l'influence du learning rate.

Nous poursuivrons avec une étude du Dropout pour
examiner l'effet de la régularisation sur la
généralisation du CNN.
