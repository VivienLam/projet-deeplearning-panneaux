
## 11.9 - Synthèse du système YOLO + CNN

### 1. Objectif du système

Notre projet repose sur deux opérations :

- **YOLO** recherche et localise les panneaux dans une scène routière.
- **CNN** classe les panneaux détectés parmi 43 catégories GTSRB.

Le MLP constitue un modèle de référence pour comparer
les performances des architectures de classification.

### 2. Évaluation du détecteur YOLO

L'évaluation exploratoire sur les 600 scènes GTSDB
donne les résultats suivants :

| Indicateur | Valeur |
|---|---:|
| Vrais positifs | 749 |
| Faux positifs | 1061 |
| Faux négatifs | 103 |
| Précision | 41.38 % |
| Rappel | 87.91 % |
| F1-score | 56.27 % |

Ces métriques concernent la localisation des panneaux,
et non leur classification.

Elles dépendent de la méthode d'association des rectangles
et ne constituent pas une évaluation indépendante.

### 3. Comparaison MLP et CNN sur GTSRB

Les deux modèles sont évalués sur les mêmes
**12630 images du test officiel GTSRB**.

| Indicateur | MLP | CNN |
|---|---:|---:|
| Accuracy | 85.22 % | 95.78 % |
| Précision macro | 82.81 % | 95.42 % |
| Rappel macro | 79.66 % | 93.18 % |
| F1-score macro | 80.12 % | 93.81 % |

**Interprétation :** Le CNN dépasse le MLP de 10.56 points d'accuracy.

Le CNN utilise des convolutions pour exploiter
la structure spatiale des images, tandis que le MLP
traite les pixels après aplatissement.

### 4. Fonctionnement du pipeline

Le système complet suit les étapes suivantes :

1. Charger une scène routière.
2. Détecter les panneaux avec YOLO.
3. Extraire les régions détectées.
4. Redimensionner et normaliser ces régions.
5. Classer chaque région avec notre CNN.
6. Afficher les catégories prédites sur l'image.

### 5. Limites de l'évaluation

La détection YOLO a été évaluée sur des scènes GTSDB,
tandis que le CNN a été évalué sur des images GTSRB.

Ces performances ne doivent pas être confondues.

Les 300 scènes GTSDB de test ont servi
à démontrer le fonctionnement du pipeline,
mais nous ne disposons pas d'une évaluation
indépendante fiable du système complet sur ces scènes.

Nous ne pouvons donc pas déduire une accuracy
globale YOLO + CNN à partir des métriques séparées.

### 6. Conclusion

Nous avons construit un système combinant la
localisation automatique de panneaux et leur
classification.

L'étude du MLP et du CNN permet de comparer
deux architectures de reconnaissance d'images.

L'étude de YOLO met en évidence les difficultés
supplémentaires liées à la détection de panneaux
dans une scène routière complète.

Une prochaine étape serait d'améliorer la localisation
et d'évaluer le pipeline de bout en bout sur un
ensemble indépendant correctement annoté.
