# 🚦 Projet Deep Learning — Reconnaissance de panneaux de signalisation

Projet ING3 — Module : Fondamentaux du Deep Learning  
Auteur : Vivien LAMBERT (Groupe A)  
Formatrice : Hanane Zerdoum  

## Description
Ce projet vise à développer un système de vision par ordinateur pour la reconnaissance automatique de panneaux de signalisation routière, à partir du jeu de données **GTSRB** (*German Traffic Sign Recognition Benchmark*, 43 classes, plus de 50 000 images).

Le projet s'articule autour des étapes suivantes :
1. **Partie 1 :** Compréhension, analyse exploratoire (EDA) et préparation des données.
2. **Partie 2 :** Modèle de référence dense (MLP).
3. **Partie 3 :** Construction d'un réseau convolutif profond (CNN) avec Keras.
4. **Partie 4 :** Entraînement et analyse de convergence.
5. **Partie 5 :** Évaluation finale et analyse d'erreurs.
6. **Partie 6 :** Expérimentations et Data Augmentation.
7. **Extensions :** Détection d'objets (YOLO) et application vidéo.

## Structure du dépôt
- `Projet_DeepLearning.ipynb` : Notebook principal du projet.
- `download_data.py` : Script pour télécharger et décompresser le dataset GTSRB.
- `prepare_dataset.py` : Script de prétraitement et mise en cache (32x32).
- `Projet_DL_Groupe_A_Panneaux_signalisation.pdf` : Sujet du projet.

## Installation et exécution

1. **Cloner le dépôt :**
   ```bash
   git clone <URL_DU_DEPOT>
   cd <DOSSIER>
   ```

2. **Installer les bibliothèques requises :**
   ```bash
   pip install tensorflow opencv-python pandas matplotlib seaborn scikit-learn
   ```

3. **Télécharger les données GTSRB :**
   ```bash
   python download_data.py
   ```

4. **Exécuter le notebook :**
   Ouvrir `Projet_DeepLearning.ipynb` dans VS Code ou Jupyter.
