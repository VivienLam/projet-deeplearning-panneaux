
## Partie 9 — Conclusion générale du projet

### 9.1 Rappel de l'objectif

L'objectif de notre projet était de développer un système
de reconnaissance automatique de panneaux de signalisation
à partir d'images du dataset GTSRB.

Le problème étudié est une classification d'images en
43 catégories.

### 9.2 Travail réalisé

Notre démarche s'est organisée autour de plusieurs étapes :

1. Recherche, compréhension et préparation des données.
2. Construction et entraînement d'un réseau Dense (MLP).
3. Construction et entraînement d'un CNN.
4. Analyse des courbes et des erreurs de classification.
5. Expérimentations sur le learning rate, le Dropout
   et l'augmentation des données.
6. Sélection du meilleur CNN sur les données de validation.
7. Évaluation finale sur le jeu de test officiel.
8. Comparaison des performances du MLP et du CNN.

### 9.3 Résultats principaux

Les deux architectures ont été évaluées sur les mêmes
12630 images du test officiel.

| Indicateur | MLP | CNN |
|---|---:|---:|
| Accuracy | 85.22 % | 95.78 % |
| Précision macro | 82.81 % | 95.42 % |
| Rappel macro | 79.66 % | 93.18 % |
| F1-score macro | 80.12 % | 93.81 % |

Le CNN améliore l'accuracy de **+10.56 points**
par rapport au MLP.

Son F1-score macro est supérieur de
**+13.70 points**.

### 9.4 Apport des expérimentations

Les expériences ont permis d'étudier l'effet de plusieurs
choix de configuration sur les performances du CNN.

Le modèle retenu après comparaison sur la validation est :

**Avec Dropout**

Il a obtenu :

- Accuracy de validation :
  99.35 %
- Loss de validation :
  0.0344

Les résultats des expériences restent propres aux
configurations étudiées et ne démontrent pas qu'une
technique serait systématiquement supérieure.

### 9.5 Performances sur le test officiel

Le CNN sélectionné a obtenu :

- Accuracy test : 95.78 %
- Loss test : 0.2226
- Images correctement classées :
  12097
- Images incorrectement classées :
  533

L'écart d'accuracy entre test et validation est
de **-3.57 points**.

Cet écart montre l'intérêt d'une évaluation sur un
ensemble indépendant de celui utilisé pour sélectionner
les hyperparamètres.

### 9.6 Limites et perspectives

Malgré ses bonnes performances globales, le CNN commet
encore des erreurs, notamment sur certaines catégories
visuellement proches.

Les résultats peuvent dépendre du découpage des données,
de l'initialisation et des conditions d'acquisition.

Une perspective serait de répéter les expériences avec
plusieurs graines aléatoires et d'étudier d'autres
architectures CNN.

Il serait également intéressant d'évaluer les performances
sur des images présentant d'autres conditions de luminosité,
de résolution ou de cadrage.

### 9.7 Conclusion

Ce projet nous a permis de mettre en pratique les notions
fondamentales du Deep Learning : réseaux Dense, convolutions,
fonctions d'activation, entraînement, régularisation et
évaluation des modèles.

Dans notre expérimentation, le CNN a obtenu de meilleures
performances que le MLP pour la reconnaissance des panneaux
de signalisation GTSRB.

L'analyse des erreurs et la comparaison des configurations
montrent qu'il est essentiel de ne pas se limiter à
l'accuracy d'entraînement, mais d'étudier également
la généralisation et les limites des modèles.
