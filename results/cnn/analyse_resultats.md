
### 4.9 Analyse et interprétation des résultats

#### 1. Résultats de l'entraînement

Nous avons entraîné notre CNN pendant **15 époques**,
avec l'optimiseur Adam et un batch size de 64.

À la dernière époque, nous obtenons :

| Métrique | Résultat |
|---|---:|
| Accuracy entraînement | 99.86 % |
| Accuracy validation | 99.25 % |
| Loss entraînement | 0.0058 |
| Loss validation | 0.0450 |

La meilleure époque selon la perte de validation est
**l'époque 15**.

À cette époque, la loss de validation est de
**0.0450** et l'accuracy correspondante
est de **99.25 %**.

#### 2. Analyse de l'accuracy

L'accuracy d'entraînement passe de
**64.50 %** à **99.86 %**.

L'accuracy de validation passe de
**90.65 %** à **99.25 %**.

L'écart final entre les performances d'entraînement
et de validation est de **0.61
point(s) de pourcentage**.

Ces valeurs permettent d'étudier la progression
de l'apprentissage et la capacité du réseau à
généraliser sur les données de validation.

#### 3. Analyse de la fonction de perte

La loss d'entraînement évolue de
**1.3093** à **0.0058**.

La loss de validation évolue de
**0.3582** à **0.0450**.

Nous observons **5 augmentation(s)**
de la loss de validation entre deux époques consécutives.

Ces fluctuations doivent être étudiées conjointement
avec les courbes d'accuracy.

#### 4. Analyse du surapprentissage

La plus faible perte de validation est obtenue à la dernière époque. Les résultats ne montrent pas de dégradation finale durable selon ce critère. Cela ne suffit toutefois pas à exclure tout surapprentissage.

L'analyse de la généralisation devra être complétée
par une étude des erreurs et une évaluation finale
sur le jeu de test indépendant.

#### 5. Conclusion

Ce premier CNN constitue notre modèle de référence.

Son meilleur état selon la perte de validation a été
conservé grâce à ModelCheckpoint.

Dans la suite du projet, nous étudierons les erreurs
de classification et comparerons plusieurs configurations
du CNN pour déterminer les améliorations pertinentes.
