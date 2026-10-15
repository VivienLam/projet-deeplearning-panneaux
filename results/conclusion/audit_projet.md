
## 12.1 — Rapport de vérification du projet

### Vérification des ressources

| Ressource | Etat |
|---|---|
| Images GTSRB | OK |
| Test GTSRB | OK |
| Annotations GTSRB | OK |
| Scènes GTSDB train | OK |
| Scènes GTSDB test | OK |
| Annotations GTSDB | OK |
| Modèle MLP | OK |
| Meilleur CNN initial | OK |
| CNN avec Dropout | OK |
| Métriques YOLO | OK |
| Synthèse finale | OK |

**Ressources trouvées : 11/11**

### Structure du notebook

- Nombre total de cellules : 82
- Cellules Python : 60
- Cellules Markdown : 22

### Vérification méthodologique

Les résultats de classification MLP/CNN sont issus
du jeu de test GTSRB.

Les métriques de détection YOLO présentées dans
le projet concernent les scènes historiques GTSDB
sur lesquelles l'évaluation a été réalisée.

Il est nécessaire de distinguer ces évaluations.

### Conclusion de l'audit

Cette étape vérifie la présence des fichiers et
la structure du notebook.

Elle ne garantit pas encore que toutes les cellules
s'exécutent correctement après redémarrage du noyau.
