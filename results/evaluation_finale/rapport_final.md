
### 7.7 Analyse et interprétation de l'évaluation finale

#### 1. Modèle évalué

Après trois expériences comparatives, nous avons sélectionné
le modèle **Avec Dropout** selon la plus faible
perte de validation.

Nous l'avons évalué sur les **12630
images du jeu de test officiel GTSRB**.

#### 2. Résultats obtenus

| Indicateur | Valeur |
|---|---:|
| Accuracy test | 95.78 % |
| Loss test | 0.2226 |
| Précision macro | 95.42 % |
| Rappel macro | 93.18 % |
| F1-score macro | 93.81 % |
| Images correctes | 12097 |
| Images incorrectes | 533 |

#### 3. Comparaison validation et test

- Accuracy de validation : **99.35 %**
- Accuracy de test : **95.78 %**
- Différence test - validation : **-3.57 point(s)**

Cet écart indique la différence observée entre les
performances du modèle sur les deux ensembles.

Les images de test n'ont pas servi à sélectionner
les hyperparamètres du CNN.

#### 4. Catégories les plus difficiles

Les cinq classes présentant les rappels les plus faibles
sur le test officiel sont :

| Classe | Rappel | Nombre d'images |
|---|---:|---:|
| Fin interdiction depassement | 58.33 % | 60 |
| Verglas / neige | 67.33 % | 150 |
| Passage pietons | 71.67 % | 60 |
| Limitation 20 km/h | 71.67 % | 60 |
| Succession de virages | 76.67 % | 90 |

#### 5. Principales confusions

- **Fin interdiction depassement** prédit comme **Depassement interdit** : 24 erreur(s).
- **Verglas / neige** prédit comme **Cyclistes** : 22 erreur(s).
- **Contournement droite** prédit comme **Tout droit ou gauche** : 18 erreur(s).
- **Limitation 100 km/h** prédit comme **Limitation 80 km/h** : 16 erreur(s).
- **Limitation 60 km/h** prédit comme **Limitation 80 km/h** : 16 erreur(s).

Ces erreurs permettent d'identifier les catégories
qui sont le plus souvent confondues par le modèle.

L'observation des images mal classées permet de
rechercher des facteurs explicatifs possibles.

#### 6. Limites de l'étude

Les résultats proviennent d'un seul jeu de test
officiel et d'expériences réalisées principalement
une fois par configuration.

Nous ne pouvons pas garantir que les performances
seront identiques sur des images provenant d'autres
caméras, pays ou conditions d'acquisition.

#### 7. Conclusion

Notre projet a permis de construire et d'évaluer
un réseau de neurones convolutif pour la reconnaissance
de 43 catégories de panneaux de signalisation.

Nous avons étudié l'influence du learning rate,
du Dropout et de l'augmentation des données.

Le modèle retenu a obtenu une accuracy de test
de **95.78 %**.

L'analyse des erreurs et des métriques par classe
permet de compléter cette performance globale
et d'identifier les limites du système.
