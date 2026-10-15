# Reconnaissance et détection de panneaux de signalisation — Deep Learning

Projet de vision par ordinateur consacré à la **classification de panneaux routiers**, à leur **détection dans des scènes** et à l'**analyse de vidéos**. L'approche combine un réseau dense (MLP), un réseau convolutif (CNN) et un détecteur YOLO associé au CNN.

> **Notebook principal :** `Projet_DeepLearning.ipynb`  
> **Environnement conseillé :** Python 3.12, Conda/Miniforge et Jupyter (VS Code ou JupyterLab).  
> **Important :** les jeux de données et les poids de modèles peuvent être volumineux ; ils ne sont pas nécessairement inclus dans le dépôt Git.

## Sommaire

1. [Objectifs et fonctionnement](#objectifs-et-fonctionnement)
2. [Technologies](#technologies)
3. [Arborescence du dépôt](#arborescence-du-dépôt)
4. [Téléchargement des données](#téléchargement-des-données)
5. [Installation de l'environnement](#installation-de-lenvironnement)
6. [Exécution du notebook](#exécution-du-notebook)
7. [Modèles et résultats](#modèles-et-résultats)
8. [Reproduction de l'analyse vidéo](#reproduction-de-lanalyse-vidéo)
9. [Dépannage](#dépannage)
10. [Références et conditions d'utilisation](#références-et-conditions-dutilisation)

## Objectifs et fonctionnement

Le travail suit une progression en plusieurs phases :

1. **Préparer GTSRB** : explorer les classes, redimensionner les images en `32 × 32 × 3`, normaliser les pixels et encoder les 43 catégories.
2. **Établir une référence MLP** : entraîner et évaluer un réseau entièrement connecté.
3. **Entraîner un CNN** : apprendre automatiquement les caractéristiques visuelles des panneaux.
4. **Évaluer les performances** : accuracy, loss, matrices de confusion, rapports de classification et analyse des erreurs.
5. **Comparer des expériences** : variation du *learning rate*, Dropout et augmentation de données.
6. **Évaluer le modèle retenu** sur le jeu de test officiel, non utilisé pour le choix des hyperparamètres.
7. **Détecter les panneaux** dans des scènes à l'aide de YOLO.
8. **Traiter une vidéo** : YOLO localise les régions contenant des panneaux, puis le CNN classe les panneaux extraits.

### Différence entre classification et détection

- **CNN (classification)** : reçoit une image contenant déjà un panneau et retourne une classe parmi les **43 classes GTSRB**.
- **YOLO (détection)** : reçoit une scène complète et retourne des boîtes englobantes autour des objets reconnus par le détecteur.
- **YOLO + CNN** : applique successivement ces deux étapes aux images d'une vidéo.

**Limite importante :** un détecteur YOLO généraliste ne garantit pas la détection des panneaux de circulation ; les résultats dépendent des classes sur lesquelles **les poids YOLO utilisés** ont été entraînés. De même, le CNN a été appris sur des panneaux allemands ; une vidéo filmée dans un autre pays peut provoquer des erreurs.

## Technologies

| Outil / bibliothèque | Rôle |
| --- | --- |
| Python 3.12 | Développement du pipeline |
| TensorFlow 2.21 / Keras 3.15 | MLP, CNN, entraînement et inférence |
| PyTorch | Exécution du détecteur YOLO via Ultralytics |
| Ultralytics YOLO 8.4 | Détection d'objets dans les images et vidéos |
| OpenCV | Lecture, conversion RGB, redimensionnement et écriture vidéo |
| NumPy | Tableaux d'images, normalisation et prédictions |
| Pandas | Lecture des annotations et export des résultats CSV |
| Scikit-learn | Séparation stratifiée, métriques et rapports |
| Matplotlib / Seaborn | Graphiques et matrices de confusion |
| Pillow | Manipulation d'images (dépendance utile) |
| FFmpeg | Inspection et conversion éventuelle des vidéos |
| VS Code + extensions Python/Jupyter, ou JupyterLab | Exécution du notebook |
| Conda / Miniforge | Gestion de l'environnement |
| Git | Versionnement du projet |

### Matériel recommandé

- Windows 10/11 ou Linux 64 bits ;
- Python 3.12 ;
- au moins 8 Go de RAM (**16 Go ou plus** préférables) ;
- plusieurs Go d'espace disque libre pour les archives, données, caches et modèles ;
- GPU **facultatif**. Le projet fonctionne sur CPU mais l'entraînement peut être long.

La configuration native Windows testée pour ce projet utilise **PyTorch CPU**. La disponibilité d'un GPU dans l'ordinateur n'implique pas que TensorFlow ou PyTorch l'utilise automatiquement ; une configuration adaptée est nécessaire.

## Arborescence du dépôt

Structure visible dans le projet et chemins attendus par le notebook :

```text
projet-deeplearning-panneaux/
├── data/
│   ├── GTSRB/
│   │   ├── Final_Training/
│   │   │   └── Images/
│   │   │       ├── 00000/
│   │   │       ├── 00001/
│   │   │       └── .../
│   │   │           # 43 sous-dossiers : 00000 à 00042
│   │   └── Final_Test/
│   │       └── Images/
│   │           ├── 00000.ppm
│   │           └── .../
│   ├── GT-final_test.csv
│   ├── gtsrb_32x32.npz               # Cache éventuel, non indispensable
│   └── scenes/
│       └── videos/
│           └── route_test.mp4        # Vidéo fournie par l'utilisateur
├── models/
│   └── yolo/
│       └── best.pt                   # Poids du détecteur entraîné, si disponibles
├── results/
│   ├── mlp/
│   ├── cnn/
│   ├── experiences/
│   ├── evaluation_finale/
│   ├── conclusion/
│   ├── yolo/
│   └── video/
│       ├── apercu_yolo.jpg
│       ├── predictions_yolo_cnn.csv
│       ├── statistiques_yolo.csv
│       ├── video_detection_yolo.mp4
│       └── video_yolo_cnn.mp4
├── Projet_DeepLearning.ipynb
├── Projet_DL_Groupe_A_Panneaux_signalisation.pdf
├── requirements.txt
├── .gitignore
└── README.md
```

**Remarques :**
- Les fichiers placés sous `data/` doivent être ajoutés localement après téléchargement.
- Les dossiers `models/` et `results/` peuvent contenir des artefacts créés par les entraînements ou obtenus séparément. Leur présence dans cette arborescence **ne signifie pas que les fichiers de poids sont fournis avec le dépôt**.
- Certains noms ci-dessus décrivent la structure attendue pour les extensions YOLO/vidéo ; le notebook principal conservé dans le dépôt et les éventuelles cellules ajoutées localement doivent utiliser les mêmes chemins.
- Le notebook est lancé depuis **la racine du projet** afin que les chemins relatifs `data/...`, `models/...` et `results/...` soient résolus correctement.

## Téléchargement des données

### 1. GTSRB — classification (obligatoire)

**Nom complet :** *German Traffic Sign Recognition Benchmark* (43 classes).

- **Page officielle et description :** https://benchmark.ini.rub.de/gtsrb_dataset.html
- **Archive officielle de téléchargement :** https://sid.erda.dk/public/archives/daaeac0d7ce1152aea9b61d9f1e19370/published-archive.html

Dans l'archive officielle, télécharger **ces trois fichiers** :

| Fichier | Utilité |
| --- | --- |
| `GTSRB_Final_Training_Images.zip` | Images d'entraînement et annotations |
| `GTSRB_Final_Test_Images.zip` | Images du test officiel |
| `GTSRB_Final_Test_GT.zip` | Véritables étiquettes du test officiel |

**Procédure :**

1. Télécharger les trois ZIP depuis l'archive officielle.
2. Décompresser l'archive d'entraînement dans `data/` en conservant le dossier `GTSRB/Final_Training/Images/`.
3. Décompresser l'archive des images de test dans `data/` en conservant `GTSRB/Final_Test/Images/`.
4. Extraire `GT-final_test.csv` de l'archive contenant les étiquettes et le placer précisément à `data/GT-final_test.csv`.
5. Vérifier que `data/GTSRB/Final_Training/Images/00000/` contient des images `.ppm`, que les dossiers des **43 classes** existent et que le jeu de test est accessible.

> **Attention au format :** certains miroirs (notamment Kaggle) proposent `Train/`, `Test/` et `Train.csv` / `Test.csv` au format PNG. **Cette disposition n'est pas directement compatible avec les chemins et les images PPM attendus par ce notebook.** Pour exécuter le code sans modifications, utiliser les archives officielles indiquées ci-dessus.

**Répartition de référence :**

| Ensemble | Nombre d'images |
| --- | ---: |
| Entraînement GTSRB officiel avant découpage | 39 209 |
| Entraînement interne après séparation 80/20 | 31 367 |
| Validation interne | 7 842 |
| Test officiel | 12 630 |
| Nombre de classes | 43 |

Les effectifs internes correspondent au découpage effectué dans le notebook (`test_size=0.20`, `random_state=42`, séparation stratifiée). Le test officiel reste séparé de l'entraînement.

#### Vérification rapide des chemins

Depuis la racine du projet, avec l'environnement activé :

```bash
python -c "from pathlib import Path; xs=['data/GTSRB/Final_Training/Images','data/GTSRB/Final_Test/Images','data/GT-final_test.csv']; [print(('OK' if Path(p).exists() else 'MANQUANT'),p) for p in xs]"
```

Toutes les lignes doivent afficher `OK`.

### 2. GTSDB — détection dans des scènes (extension YOLO)

**Nom complet :** *German Traffic Sign Detection Benchmark*.

- **Page officielle :** https://benchmark.ini.rub.de/gtsdb_dataset.html
- **Archive officielle :** https://sid.erda.dk/public/archives/ff17dc924eba88d5d01a807357d6614c/published-archive.html

Le jeu comprend **900 scènes** (600 images historiquement affectées à l'entraînement et 300 à l'évaluation). L'archive complète `FullIJCNN2013.zip` contient les scènes et leurs annotations.

Pour la partie détection, télécharger **`FullIJCNN2013.zip`**, puis le décompresser, par exemple, dans `data/GTSDB/` si la cellule ou le script de détection utilise ce chemin.

**Important :** les annotations GTSDB ne sont **pas directement au format YOLO**. En cas d'entraînement d'un détecteur Ultralytics sur GTSDB, il faut :
- convertir les boîtes et étiquettes du format original au format YOLO ;
- effectuer une séparation entraînement/validation sans fuite de données ;
- créer un fichier de configuration de données `*.yaml` décrivant les images et les classes ;
- entraîner YOLO puis conserver ses poids (`best.pt`).

Le simple téléchargement de GTSDB **ne crée pas automatiquement** `models/yolo/best.pt`. Le dépôt doit fournir un script/notebook de préparation et d'entraînement, ou des poids déjà entraînés séparément.

### 3. Vidéo de démonstration (extension vidéo)

Pour l'analyse de vidéos, prévoir une séquence montrant une route et des panneaux de signalisation.

**Chemin attendu par la cellule YOLO + CNN vérifiée :**

```text
data/scenes/videos/route_test.mp4
```

Une vidéo personnelle, librement réutilisable ou utilisée avec l'autorisation nécessaire convient. **Aucune vidéo précise n'est fournie par les benchmarks GTSRB/GTSDB**, qui sont des jeux d'images. La vidéo de démonstration doit donc être fournie séparément.

Le détecteur entraîné est attendu ici :

```text
models/yolo/best.pt
```

Le classificateur CNN utilisé par le pipeline vidéo est attendu ici :

```text
results/experiences/exp2_dropout/avec_dropout/meilleur_modele.keras
```

Sans ces deux modèles et la vidéo d'entrée, l'exécution de la partie YOLO + CNN échouera, même si les bibliothèques Python sont installées.

## Installation de l'environnement

### 1. Récupérer le code

Cloner le dépôt depuis son URL GitHub réelle (bouton **Code → HTTPS**) ou télécharger le ZIP du dépôt, puis ouvrir le dossier `projet-deeplearning-panneaux` dans VS Code.

Dans un terminal ouvert **à la racine du projet** :

```bash
conda create -n dsai python=3.12 pip -y
conda activate dsai
```

L'environnement `dsai` est un nom proposé : il peut être remplacé pour éviter tout conflit avec un environnement existant.

### 2. Installer les outils système et OpenCV

```bash
conda install -c conda-forge opencv ffmpeg ipykernel jupyterlab -y
```

### 3. Installer PyTorch

**Option CPU sur Windows 64 bits, Python 3.12 (configuration utilisée pendant les tests) :**

```bash
python -m pip install torch==2.14.0 torchvision==0.29.0 torchaudio==2.11.0 --index-url https://download.pytorch.org/whl/cpu
```

Pour Linux et les configurations avec GPU, choisir les commandes correspondant à la machine depuis le configurateur officiel : https://pytorch.org/get-started/locally/

### 4. Installer les bibliothèques du projet

```bash
python -m pip install -r requirements.txt
```

Le fichier `requirements.txt` contient les dépendances principales. **Il ne représente pas un verrouillage exhaustif de toutes les dépendances système et de tous les paquets transitifs** ; les versions disponibles peuvent évoluer. Pour une reproduction scientifique exacte, il est conseillé d'archiver également l'export de l'environnement complet testé.

### 5. Vérifier les imports et le noyau Jupyter

```bash
python -m pip check
python -c "import tensorflow, torch, ultralytics, cv2, numpy, pandas, sklearn; print('Imports principaux : OK')"
python -m ipykernel install --user --name dsai --display-name "Python (dsai)"
```

Le message `No broken requirements found.` signale l'absence de conflits **déclarés** par pip. Il ne remplace pas le test réel de toutes les fonctionnalités.

## Exécution du notebook

### Avec VS Code

1. Ouvrir le dossier du projet (**File → Open Folder**).
2. Installer les extensions **Python** et **Jupyter** si elles ne sont pas déjà présentes.
3. Ouvrir `Projet_DeepLearning.ipynb`.
4. En haut à droite, sélectionner le noyau **Python (dsai)**.
5. Exécuter les cellules dans l'ordre.

### Avec JupyterLab

Dans le terminal à la racine du projet :

```bash
conda activate dsai
jupyter lab
```

Ouvrir `Projet_DeepLearning.ipynb` et sélectionner **Python (dsai)**.

### Ordre logique des expériences

1. Exploration du jeu GTSRB.
2. Prétraitement des images.
3. Réseau de référence MLP.
4. Réseau CNN et entraînement.
5. Courbes d'apprentissage, matrices de confusion et analyse d'erreurs.
6. Expériences : *learning rate*, Dropout et augmentation des données.
7. Sélection du CNN, évaluation finale et comparaison MLP/CNN.
8. Extensions : détection YOLO, puis YOLO + CNN sur vidéo (si leurs cellules et prérequis sont présents).

Le prétraitement initial peut prendre plusieurs minutes sur CPU lorsque les fichiers `.ppm` sont lus un par un. Une sauvegarde locale au format `.npz` peut éviter de refaire cette étape. Le notebook sait lire `data/gtsrb_32x32.npz` si ce cache existe, mais il ne faut pas supposer que ce fichier sera généré automatiquement.

## Modèles et résultats

Les sorties connues du projet sont organisées comme suit :

| Dossier | Contenu |
| --- | --- |
| `results/mlp/` | Modèle de référence `.keras`, historique d'entraînement |
| `results/cnn/` | Modèles CNN, meilleur checkpoint, courbes et historiques |
| `results/experiences/` | Comparaisons de *learning rate*, Dropout et augmentation |
| `results/evaluation_finale/` | Prédictions sur test, métriques, rapport de classification et matrice de confusion |
| `results/conclusion/` | Synthèse comparative MLP/CNN |
| `results/yolo/` | Résultats de détection, selon la version du notebook |
| `results/video/` | Images d'aperçu, CSV de détections/prédictions, vidéos annotées |

Le notebook de classification sauvegarde notamment :

```text
results/mlp/model_mlp.keras
results/cnn/cnn_meilleur.keras
results/experiences/exp2_dropout/avec_dropout/meilleur_modele.keras
results/evaluation_finale/predictions_test.csv
```

Pour **réutiliser** un modèle, le fichier `.keras` ou `.pt` correspondant doit être présent. Pour **reproduire l'entraînement**, il faut les données et les cellules d'entraînement ; les résultats exacts peuvent varier selon les paramètres, versions et ressources matérielles.

## Reproduction de l'analyse vidéo

La cellule YOLO + CNN configurée pour ce projet utilise :

```text
Entrée vidéo : data/scenes/videos/route_test.mp4
Détecteur   : models/yolo/best.pt
CNN         : results/experiences/exp2_dropout/avec_dropout/meilleur_modele.keras
Sortie MP4  : results/video/video_yolo_cnn.mp4
Sortie CSV  : results/video/predictions_yolo_cnn.csv
```

**Vérifications :**

```bash
python -c "from pathlib import Path; xs=['data/scenes/videos/route_test.mp4','models/yolo/best.pt','results/experiences/exp2_dropout/avec_dropout/meilleur_modele.keras']; [print(('OK' if Path(p).is_file() else 'MANQUANT'), p) for p in xs]"
```

La version du détecteur doit contenir une classe pertinente pour les panneaux de signalisation. Un YOLO entraîné sur d'autres classes ne suffit pas nécessairement.

Ne pas confondre la **détection correcte d'une boîte** et la **classification correcte du panneau** : ces deux parties du pipeline doivent être évaluées séparément.

## Dépannage

| Erreur ou situation | Vérification / solution |
| --- | --- |
| `ModuleNotFoundError` | Vérifier le noyau Jupyter, puis installer le paquet manquant dans `dsai` |
| `FileNotFoundError` pour `data/...` | Contrôler l'arborescence et le répertoire de travail |
| `GT-final_test.csv` introuvable | Télécharger et extraire `GTSRB_Final_Test_GT.zip` |
| Les images `Train/` sont en PNG | Variante de dataset différente : utiliser les archives officielles PPM ou adapter le code |
| `models/yolo/best.pt` manquant | Entraîner/récupérer les poids du détecteur ; GTSDB seul ne suffit pas |
| Vidéo introuvable | Placer le MP4 à `data/scenes/videos/route_test.mp4` ou adapter la cellule |
| TensorFlow / PyTorch fonctionne lentement | Vérifier CPU/GPU ; un environnement CPU peut être nettement plus lent |
| `No space left on device` | Libérer de l'espace ; nettoyer si nécessaire les caches `python -m pip cache purge` et `conda clean --all -y` |
| Mauvaises classes sur des panneaux étrangers | Décalage entre les 43 classes GTSRB allemandes et les panneaux présents dans la vidéo |

Pour vérifier l'environnement actif :

```bash
python --version
python -m pip check
```

Sur Windows, `where python` indique le chemin de l'interpréteur ; sur Linux, utiliser `which python`.

## Références et conditions d'utilisation

**Benchmarks officiels :**
- GTSRB : https://benchmark.ini.rub.de/gtsrb_dataset.html
- Téléchargement GTSRB : https://sid.erda.dk/public/archives/daaeac0d7ce1152aea9b61d9f1e19370/published-archive.html
- GTSDB : https://benchmark.ini.rub.de/gtsdb_dataset.html
- Téléchargement GTSDB : https://sid.erda.dk/public/archives/ff17dc924eba88d5d01a807357d6614c/published-archive.html

**Documentation technique :**
- TensorFlow : https://www.tensorflow.org/
- Keras : https://keras.io/
- PyTorch : https://pytorch.org/
- Ultralytics : https://docs.ultralytics.com/
- Scikit-learn : https://scikit-learn.org/
- OpenCV : https://opencv.org/

**Publications à citer :**
- J. Stallkamp, M. Schlipsing, J. Salmen et C. Igel (2011), *The German Traffic Sign Recognition Benchmark: A multi-class classification competition*, IJCNN.
- S. Houben, J. Stallkamp, J. Salmen, M. Schlipsing et C. Igel (2013), *Detection of Traffic Signs in Real-World Images: The German Traffic Sign Detection Benchmark*, IJCNN.

Les auteurs de GTSRB indiquent que les données sont libres d'utilisation tout en demandant de citer la publication associée. Consulter les archives officielles pour les modalités de réutilisation et veiller aux droits sur les vidéos éventuellement ajoutées.

---

**Statut de la documentation :** le README reprend les chemins réels du notebook de classification examiné, la structure visible du projet et la configuration vérifiée de la cellule vidéo YOLO + CNN. Les poids `best.pt`, le contenu exact du jeu de données YOLO converti et le dépôt GitHub distant n'ont pas été fournis ici : leurs liens ne sont donc pas inventés.
