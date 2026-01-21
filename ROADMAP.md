# ROADMAP - Prédiction Émissions CO2 Seattle

## Vue d'ensemble selon la méthode BMAD

Cette roadmap applique la **méthode BMAD (Business Model Agile Design)** au projet de prédiction des émissions de CO2 et de consommation énergétique des bâtiments de Seattle.

---

## 🎯 B - BUSINESS (Contexte et Valeur)

### Problématique Business
La ville de Seattle s'est fixé l'objectif ambitieux d'atteindre la **neutralité carbone d'ici 2050**. Pour y parvenir, il est crucial de :
- Comprendre les sources d'émissions des bâtiments non résidentiels
- Identifier les bâtiments à fort impact environnemental
- Prioriser les actions de rénovation énergétique
- Mesurer l'impact des politiques publiques

### Proposition de Valeur
Ce projet fournit :
- **Prédictions précises** des émissions CO2 et consommation énergétique
- **Insights actionnables** sur les facteurs clés d'émissions
- **Outil d'aide à la décision** pour les planificateurs urbains
- **Base analytique** pour le suivi des objectifs climatiques

### Parties Prenantes
- **Ville de Seattle** : Planification des politiques environnementales
- **Propriétaires de bâtiments** : Identification des opportunités d'optimisation
- **Citoyens** : Transparence sur l'empreinte carbone des bâtiments
- **Chercheurs** : Données et modèles pour études environnementales

---

## 🔬 M - MODEL (Architecture et Modélisation)

### Phase 1 : Exploration et Compréhension des Données ✅ (TERMINÉ)

**Objectif** : Comprendre la structure, qualité et patterns des données

**Livrables** :
- [x] Notebook d'exploration (Explo.ipynb / 01_exploration.ipynb)
- [x] Analyse de la distribution des variables
- [x] Détection des outliers et valeurs aberrantes
- [x] Analyse de corrélation
- [x] Visualisations exploratoires

**Résultats clés** :
- 1,650 bâtiments non résidentiels analysés
- 40+ features après preprocessing
- Identification des features critiques (PropertyGFATotal, ENERGYSTARScore, Age)

---

### Phase 2 : Preprocessing et Feature Engineering ✅ (TERMINÉ)

**Objectif** : Préparer les données pour la modélisation

**Tâches réalisées** :
- [x] Filtrage des bâtiments multifamiliaux
- [x] Suppression des outliers
- [x] Imputation des valeurs manquantes (IterativeImputer)
- [x] One-Hot Encoding des variables catégorielles
- [x] Création de features dérivées (Age, ratios de surface, % énergies)
- [x] Normalisation (StandardScaler)
- [x] Transformations log1p pour features asymétriques

**Dataset final** :
- 1,648 observations
- 40 features (19 numériques, 21 catégorielles encodées)
- 0 valeurs manquantes

---

### Phase 3 : Modélisation et Optimisation ✅ (TERMINÉ)

**Objectif** : Développer des modèles prédictifs performants

#### Sprint 1 : Modèles Linéaires
- [x] Baseline (DummyRegressor)
- [x] Linear Regression
- [x] Ridge Regression + GridSearch
- [x] Lasso Regression + GridSearch
- [x] TransformedTargetRegressor variants

**Meilleur résultat** : Ridge (RMSE: 17.8M)

#### Sprint 2 : Support Vector Machines
- [x] SVR avec différents kernels
- [x] TransformedTarget SVR
- [x] GridSearchCV sur C, degree, kernel

**Meilleur résultat** : TT-SVR (RMSE: 15.3M)

#### Sprint 3 : Ensembles Methods
- [x] Random Forest + hyperparameter tuning
- [x] Gradient Boosting + tuning
- [x] AdaBoost + tuning
- [x] XGBoost + tuning
- [x] Variants avec TransformedTarget

**Meilleur résultat** : **Random Forest (RMSE: 12.9M)** 🏆

#### Sprint 4 : Neural Networks
- [x] MLPRegressor
- [x] GridSearch sur architecture et activations
- [x] Variants avec transformation de target

**Résultat** : MLP (RMSE: 22.1M) - moins performant

---

### Phase 4 : Interprétabilité et Analyse ✅ (TERMINÉ)

**Objectif** : Comprendre les prédictions du modèle

**Réalisations** :
- [x] Feature Importance (Random Forest, Gradient Boosting)
- [x] SHAP Values analysis
- [x] SHAP Summary Plots
- [x] SHAP Force Plots individuels
- [x] Analyse avec/sans ENERGYSTARScore

**Insights clés** :
- PropertyGFATotal est le prédicteur #1
- ENERGYSTARScore important mais non critique
- Type de bâtiment influence significativement les émissions

---

## ⚡ A - AGILE (Approche Itérative et Sprints)

### Méthodologie Agile Appliquée

Le projet a suivi une approche **itérative** avec amélioration continue :

```
Sprint 1 (Semaine 1) : Discovery
├── EDA et compréhension des données
├── Nettoyage initial
└── Baseline models

Sprint 2 (Semaine 2) : Core Modeling
├── Modèles linéaires
├── SVR
└── Premiers ensembles

Sprint 3 (Semaine 3) : Optimization
├── Random Forest tuning
├── Gradient Boosting variants
├── XGBoost
└── Hyperparameter optimization

Sprint 4 (Semaine 4) : Interpretation & Delivery
├── SHAP analysis
├── Feature importance
├── Documentation
└── Présentation
```

### Backlog Priorisé (Ce qui reste à faire)

#### Priorité HAUTE 🔴
- [ ] Créer structure de dossiers propre (data/, notebooks/, docs/)
- [ ] Renommer notebooks avec convention claire (01_, 02_, 03_)
- [ ] Nettoyer notebooks (supprimer cellules inutiles, ajouter markdown)
- [ ] Initialiser repository Git
- [ ] Faire premier commit avec structure propre

#### Priorité MOYENNE 🟡
- [ ] Ajouter des docstrings aux cellules de preprocessing
- [ ] Créer un notebook récapitulatif des résultats
- [ ] Exporter le meilleur modèle (pickle/joblib)
- [ ] Créer badges README (Python version, License, etc.)
- [ ] Ajouter images/plots dans README

#### Priorité BASSE 🟢
- [ ] Créer un script Python standalone (ml_pipeline.py)
- [ ] Ajouter tests unitaires basiques
- [ ] Dashboard interactif (Streamlit/Dash)
- [ ] Documentation API si script réutilisable
- [ ] Analyse d'erreurs sur cas extrêmes

---

## 🎨 D - DESIGN (Architecture et Organisation)

### Structure Cible du Projet

```
Projet_3_Seattle_Emissions/
│
├── data/
│   ├── raw/
│   │   └── 2016_Building_Energy_Benchmarking.csv
│   └── processed/
│       └── data_cleaned.csv
│
├── notebooks/
│   ├── 01_exploration.ipynb
│   ├── 02_preprocessing.ipynb
│   ├── 03_modeling_energy.ipynb
│   ├── 04_modeling_co2.ipynb
│   └── 05_results_summary.ipynb
│
├── src/                           (Optionnel - pour réutilisabilité)
│   ├── __init__.py
│   ├── preprocessing.py
│   ├── modeling.py
│   └── evaluation.py
│
├── models/                        (Modèles sauvegardés)
│   ├── random_forest_best.pkl
│   └── gradient_boosting_tt.pkl
│
├── docs/
│   ├── presentation.pptx          (Présentation soutenance)
│   └── methodology.md             (Documentation technique)
│
├── .gitignore
├── requirements.txt
├── README.md
├── ROADMAP.md                     (Ce fichier)
└── LICENSE                        (Optionnel)
```

### Conventions de Code

**Notebooks** :
- Nommage : `0X_description_claire.ipynb`
- Structure : Introduction → Code → Visualisations → Conclusions
- Markdown richement utilisé pour narration

**Code** :
- Style : PEP8
- Docstrings : Google style
- Comments : Français ou Anglais (cohérence)

### Workflow Git Recommandé

```bash
# Initialisation
git init
git add .
git commit -m "Initial commit - Structure projet BMAD"

# Branches
main           # Production-ready
develop        # Développement
feature/*      # Nouvelles features (optionnel pour projet solo)

# Commits conventionnels
feat: ...      # Nouvelle fonctionnalité
fix: ...       # Correction de bug
docs: ...      # Documentation
refactor: ...  # Refactoring
style: ...     # Formatage
```

---

## 📊 KPIs et Métriques de Succès

### Métriques Techniques
- ✅ **RMSE < 15M** : ATTEINT (12.9M avec Random Forest)
- ✅ **Amélioration vs baseline > 30%** : ATTEINT (45% d'amélioration)
- ✅ **R² > 0.70** : À vérifier (focus sur RMSE)

### Métriques Portfolio
- ⏳ **README complet** : EN COURS
- ⏳ **Code propre et commenté** : À AMÉLIORER
- ⏳ **Repository GitHub public** : À CRÉER
- ⏳ **Documentation professionnelle** : EN COURS

---

## 🚀 Plan d'Action Immédiat

### Cette Semaine
1. ✅ Créer .gitignore
2. ✅ Créer requirements.txt
3. ✅ Rédiger README complet
4. ✅ Créer ROADMAP.md
5. ⏳ Créer structure de dossiers
6. ⏳ Renommer et organiser notebooks
7. ⏳ Git init + premier commit

### Semaine Prochaine
1. Nettoyer notebooks (supprimer cellules debug)
2. Ajouter markdown narratif dans notebooks
3. Créer notebook de synthèse des résultats
4. Push sur GitHub
5. Ajouter badges et visuels au README

### Long Terme
- Créer version interactive (Streamlit)
- Publier article Medium/LinkedIn
- Référencer dans portfolio
- Présenter en entretien

---

## 📝 Notes et Apprentissages

### Ce qui a bien fonctionné ✅
- Approche méthodique du preprocessing
- GridSearchCV systématique pour tous les modèles
- Utilisation de SHAP pour interprétabilité
- TransformedTargetRegressor améliore certains modèles

### Challenges rencontrés ⚠️
- Imputation des valeurs manquantes (IterativeImputer long)
- GridSearchCV très chronophage (optimiser avec RandomizedSearchCV)
- ENERGYSTARScore : utile mais crée de la fuite de données potentielle
- Temps de calcul élevé pour certains modèles (XGBoost, MLP)

### Améliorations futures 🔮
- Utiliser Optuna pour hyperparameter tuning (plus rapide)
- Tester des features polynomiales
- Stacking/Blending de modèles
- Validation sur données 2017-2018 si disponibles
- Analyse géospatiale (clustering par quartier)

---

**Version** : 1.0
**Dernière mise à jour** : Janvier 2024
**Méthode** : BMAD (Business Model Agile Design)
**Statut** : 🟢 En finalisation
