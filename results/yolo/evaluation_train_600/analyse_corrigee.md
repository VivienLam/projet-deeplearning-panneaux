
## 11.8 - Analyse des résultats YOLO

### Objectif

Nous évaluons le détecteur YOLO sur les 600 scènes du
jeu d'entraînement historique GTSDB, à partir des annotations
locales vérifiées.

### Données utilisées

- Scènes considérées : **600**
- Scènes avec annotations : **506**
- Scènes sans annotation : **94**
- Panneaux annotés : **852**
- Seuil de confiance : **0.25**
- Seuil IoU enregistré : **0.5**

### Résultats de localisation

| Indicateur | Résultat |
|---|---:|
| Vrais positifs (VP) | 749 |
| Faux positifs (FP) | 1061 |
| Faux négatifs (FN) | 103 |
| Précision | 41.38 % |
| Rappel | 87.91 % |
| F1-score | 56.27 % |

### Interprétation

La précision de **41.38 %** représente la
proportion des détections considérées correctes parmi
toutes les détections du modèle, selon notre protocole.

Le rappel de **87.91 %** représente la
proportion des panneaux annotés qui ont été retrouvés.

Le F1-score de **56.27 %** combine
la précision et le rappel.

### Limites méthodologiques

Ces résultats dépendent de notre méthode d'association
des rectangles prédits aux annotations, du seuil IoU
et du seuil de confiance.

La correspondance doit être effectuée sans associer
plusieurs prédictions à une même annotation.

Ces résultats ne sont pas des métriques officielles
du jeu de test GTSDB de 300 scènes.

Nos prédictions sur ces 300 scènes sont conservées
comme démonstration du pipeline YOLO + CNN,
mais leur précision ne peut pas être calculée
avec le fichier d'annotations actuellement utilisé.

### Conclusion

Nous disposons d'une première évaluation quantitative
de la localisation des panneaux sur les scènes annotées.

Cette évaluation doit être distinguée de la classification
des panneaux par notre CNN et des démonstrations réalisées
sur les 300 scènes de test.
