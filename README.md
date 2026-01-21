# Prédiction des Émissions de CO2 et Consommation Énergétique - Ville de Seattle

![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=flat&logo=python&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-1.0+-F7931E?style=flat&logo=scikit-learn&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-1.3+-150458?style=flat&logo=pandas&logoColor=white)
![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-F37626?style=flat&logo=jupyter&logoColor=white)
![XGBoost](https://img.shields.io/badge/XGBoost-1.5+-FF6600?style=flat)
![SHAP](https://img.shields.io/badge/SHAP-Interpretability-00BFFF?style=flat)
![License](https://img.shields.io/badge/License-MIT-green?style=flat)
![Status](https://img.shields.io/badge/Status-Completed-success?style=flat)

## Contexte du Projet

Ce projet a été réalisé dans le cadre de l'objectif ambitieux de la ville de Seattle d'atteindre la **neutralité carbone d'ici 2050**. L'analyse porte sur les bâtiments non résidentiels et vise à prédire leurs émissions de CO2 et leur consommation totale d'énergie à partir de caractéristiques structurelles.

## Objectifs

- Prédire les **émissions de CO2** des bâtiments non résidentiels
- Prédire la **consommation totale d'énergie** des bâtiments
- Identifier les facteurs clés influençant ces métriques
- Fournir des insights pour aider la ville dans sa stratégie de réduction des émissions

## Jeu de Données

**Source** : [2016 Building Energy Benchmarking](https://data.seattle.gov/dataset/2016-Building-Energy-Benchmarking/2bpz-gwpy)

- **Période** : Données de 2016
- **Scope** : Bâtiments non résidentiels de Seattle
- **Observations** : ~1,650 bâtiments après nettoyage
- **Variables** : 40+ features incluant :
  - Caractéristiques structurelles (surface, nombre d'étages, âge)
  - Type de propriété
  - Consommation énergétique (électricité, gaz naturel, vapeur)
  - Score ENERGY STAR
  - Localisation (district)

## Méthodologie

### 1. Exploration et Analyse des Données

**Notebook** : `01_exploration.ipynb`

- Analyse exploratoire approfondie (EDA)
- Visualisation des distributions et corrélations
- Détection et traitement des valeurs aberrantes
- Analyse des valeurs manquantes
- Feature engineering :
  - Création de la variable `Age` (DataYear - YearBuilt)
  - Ratios de surface (parking, bâtiment)
  - Pourcentages d'utilisation énergétique par source

### 2. Preprocessing et Nettoyage

- **Filtrage** : Exclusion des bâtiments multifamiliaux (focus sur non-résidentiel)
- **Traitement des outliers** : Suppression basée sur la colonne `Outlier`
- **Valeurs manquantes** : Imputation par IterativeImputer (MICE)
- **Encodage** : One-Hot Encoding pour les variables catégorielles
- **Normalisation** : StandardScaler appliqué aux features numériques
- **Transformations** : log1p sur features asymétriques (PropertyGFATotal, NumberofFloors, etc.)

### 3. Modélisation Prédictive

**Notebooks** : `02_prediction_energy.ipynb` et `03_prediction_co2.ipynb`

#### Variable Cible
- **SiteEnergyUseWN(kBtu)** : Consommation énergétique totale du site (normalisée)
- **TotalGHGEmissions** : Émissions totales de gaz à effet de serre

#### Modèles Testés

| Modèle | RMSE (meilleur) | Notes |
|--------|-----------------|-------|
| **Random Forest** | **12,877,388** | Meilleur modèle |
| Gradient Boosting (TT) | 14,282,043 | Avec transformation de target |
| AdaBoost | 14,605,126 | Performance stable |
| Random Forest (TT) | 14,733,536 | Avec transformation |
| SVR (TT) | 15,288,219 | Support Vector Regression |
| XGBoost (TT) | 15,457,243 | Bon compromis |
| Gradient Boosting | 16,706,326 | Sans transformation |
| XGBoost | 17,715,226 | Baseline XGBoost |
| Linear Regression | 20,432,949 | Modèle linéaire simple |
| Ridge | 21,623,647 | Régularisation L2 |
| Lasso | 23,144,680 | Régularisation L1 |
| **Baseline (Mean)** | 23,631,178 | Référence |

**TT** = TransformedTargetRegressor avec transformation log1p

#### Optimisation des Hyperparamètres

Utilisation de **GridSearchCV** avec validation croisée (10-fold) pour tous les modèles.

**Métriques d'évaluation** :
- RMSE (Root Mean Squared Error) - métrique principale
- MSE (Mean Squared Error)
- MAE (Mean Absolute Error)
- R² (Coefficient de détermination)

### 4. Interprétabilité

**Techniques utilisées** :
- **Feature Importance** : Identification des variables les plus influentes
- **SHAP Values** : Analyse de l'impact de chaque feature sur les prédictions
- **SHAP Force Plots** : Visualisation des contributions individuelles

#### Top Features
1. **PropertyGFATotal** : Surface totale du bâtiment
2. **LargestPropertyUseTypeGFA** : Surface de l'usage principal
3. **ENERGYSTARScore** : Score de performance énergétique
4. **Age** : Âge du bâtiment
5. **NumberofFloors** : Nombre d'étages

## Résultats Clés

- **Réduction de l'erreur de 45%** par rapport au modèle baseline (Random Forest)
- **ENERGYSTARScore** est une variable importante mais non indispensable
- Les caractéristiques **structurelles** (surface, étages) sont les prédicteurs les plus forts
- Les **types de bâtiments** (bureaux, hôtels, écoles) ont un impact significatif

## Structure du Projet

```
Projet_3/
├── data/
│   └── 2016_Building_Energy_Benchmarking.csv  # Données brutes
├── notebooks/
│   ├── 01_exploration.ipynb                   # Analyse exploratoire
│   ├── 02_prediction_energy.ipynb             # Prédiction consommation
│   └── 03_prediction_co2.ipynb                # Prédiction CO2
├── Projet_3_Thomas_Mebarki/                   # Livrables originaux
├── .gitignore
├── requirements.txt
├── README.md
└── ROADMAP.md
```

## Installation et Utilisation

### Prérequis

- Python 3.8+
- Jupyter Notebook

### Installation

```bash
# Cloner le repository
git clone https://github.com/ThomasMeb/Anticiper_besoins_des_batiments.git
cd Anticiper_besoins_des_batiments

# Créer un environnement virtuel (recommandé)
python -m venv venv
source venv/bin/activate  # Sur Windows: venv\Scripts\activate

# Installer les dépendances
pip install -r requirements.txt
```

### Exécution

```bash
# Lancer Jupyter Notebook
jupyter notebook

# Ouvrir les notebooks dans l'ordre :
# 1. notebooks/01_exploration.ipynb
# 2. notebooks/02_prediction_energy.ipynb
# 3. notebooks/03_prediction_co2.ipynb
```

## Compétences Techniques Démontrées

- **Data Science** : EDA, feature engineering, data cleaning
- **Machine Learning** : Régression, ensembles methods, hyperparameter tuning
- **Preprocessing** : Imputation, encoding, scaling, transformations
- **Évaluation** : Cross-validation, métriques multiples, model comparison
- **Interprétabilité** : Feature importance, SHAP values
- **Python** : pandas, scikit-learn, XGBoost, matplotlib, seaborn

## Améliorations Potentielles

- Collecte de données temporelles pour analyse de séries chronologiques
- Intégration de données météorologiques
- Déploiement d'un modèle en production (API REST)
- Dashboard interactif pour les décideurs
- Analyse géospatiale des émissions par quartier

## Auteur

**Thomas Mebarki**

- GitHub : [ThomasMeb](https://github.com/ThomasMeb)
- LinkedIn : [Thomas Mebarki](https://www.linkedin.com/in/thomas-mebarki/)
- Portfolio : [À venir]

## Licence

Ce projet a été réalisé à des fins éducatives dans le cadre d'une formation en Data Science.

## Remerciements

- Ville de Seattle pour la mise à disposition des données
- [OpenClassrooms / Votre organisme de formation] pour l'encadrement du projet

---

*Dernière mise à jour : Janvier 2024*
