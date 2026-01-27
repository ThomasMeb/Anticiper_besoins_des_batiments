# Schneider Electric - Energy Prediction

### Mission Freelance — Prédiction Énergétique pour Schneider Electric

![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-1.0+-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-App-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

> **Mission** : Développer un outil ML prédisant la consommation énergétique et les émissions CO2 du parc immobilier tertiaire de Schneider Electric, dans le cadre de leurs engagements **ESG et neutralité carbone**.

---

## Portfolio Notice

> **Note importante** : Ce repository est une **version portfolio** d'une mission freelance réalisée pour Schneider Electric entre novembre et décembre 2023. Pour des raisons de confidentialité, les données client ont été remplacées par le dataset public [Seattle Building Energy Benchmarking](https://data.seattle.gov/), qui présente une structure similaire. L'architecture, la méthodologie et les résultats reflètent fidèlement le travail réalisé.

---

## Résumé Exécutif

| Élément | Détail |
|---------|--------|
| **Client** | Schneider Electric — Direction Immobilier & RSE |
| **Durée** | 4 semaines (Nov-Déc 2023) |
| **Objectif** | Prédire consommation énergétique avec >30% d'amélioration vs baseline |
| **Résultat** | **45.5% d'amélioration** — Objectif dépassé |
| **Livrable** | Modèle ML + Application Web + Documentation |

### Résultats Clés

```
┌────────────────────────────────────────────────────────────────┐
│                     PERFORMANCE DU MODÈLE                       │
├────────────────────────────────────────────────────────────────┤
│                                                                │
│   Amélioration vs Baseline    ████████████████████░  45.5%    │
│                                                                │
│   Objectif Initial            ████████████░░░░░░░░░  30%      │
│                                                                │
│   Résultat : OBJECTIF DÉPASSÉ DE +15.5 POINTS                  │
│                                                                │
└────────────────────────────────────────────────────────────────┘
```

---

## Table des Matières

1. [Contexte & Problématique](#contexte--problématique)
2. [Objectifs](#objectifs)
3. [Approche & Méthodologie](#approche--méthodologie)
4. [Résultats & Impact](#résultats--impact)
5. [Demo Application](#demo-application)
6. [Installation](#installation)
7. [Contact](#contact)

---

## Contexte & Problématique

### Le Client

**Schneider Electric**, leader mondial de la gestion de l'énergie et de l'automatisation, s'est engagé dans un plan ambitieux de **neutralité carbone**. L'optimisation énergétique de leur parc immobilier tertiaire est un levier clé de cette stratégie ESG.

### La Problématique

La Direction Immobilier disposait de données sur plusieurs milliers de bâtiments mais faisait face à plusieurs défis :

| Problème | Impact |
|----------|--------|
| Analyse manuelle | 2-3 semaines par rapport |
| Méthode statistique basique | Prédictions peu fiables |
| Pas d'identification des facteurs | Impossible de prioriser les actions |
| Rapports statiques | Pas d'interactivité pour les décideurs |

### La Solution Proposée

Développer un **outil de Machine Learning** capable de :
- Prédire instantanément (<1 seconde)
- Identifier les facteurs clés d'influence
- Fournir une interface interactive
- Générer des recommandations actionnables

---

## Objectifs

| Critère | Objectif Défini | Résultat |
|---------|-----------------|----------|
| **Spécifique** | Prédire consommation énergétique et émissions CO2 | 2 modèles développés |
| **Mesurable** | RMSE inférieur de 30% au baseline | **45.5%** d'amélioration |
| **Atteignable** | Utiliser les données du parc immobilier | 1,650 bâtiments analysés |
| **Réaliste** | Stack Python/scikit-learn éprouvé | 18 modèles comparés |
| **Temporel** | Livraison sous 4 semaines | Livré dans les délais |

---

## Approche & Méthodologie

### Planning du Projet

```
TIMELINE — 4 SEMAINES
════════════════════════════════════════════════════════════════

Sem 1   │▓▓▓▓▓▓▓▓▓▓│ CADRAGE & EXPLORATION
        │          │ • Kick-off client
        │          │ • EDA préliminaire
        │          │ • Validation périmètre

Sem 2   │▓▓▓▓▓▓▓▓▓▓│ ANALYSE & PREPROCESSING
        │          │ • Nettoyage données
        │          │ • Feature engineering
        │          │ • Traitement valeurs manquantes

Sem 3   │▓▓▓▓▓▓▓▓▓▓│ MODÉLISATION
        │          │ • 18 modèles testés
        │          │ • GridSearchCV optimization
        │          │ • Validation croisée 10-fold

Sem 4   │▓▓▓▓▓▓▓▓▓▓│ LIVRAISON
        │          │ • Application Streamlit
        │          │ • Documentation
        │          │ • Présentation client

════════════════════════════════════════════════════════════════
```

### Architecture Technique

```
┌─────────────────────────────────────────────────────────────────────┐
│                        PIPELINE ML COMPLET                          │
└─────────────────────────────────────────────────────────────────────┘

    ┌──────────┐      ┌──────────┐      ┌──────────┐      ┌──────────┐
    │   DATA   │      │  CLEAN   │      │  MODEL   │      │  DEPLOY  │
    │          │ ──── │          │ ──── │          │ ──── │          │
    │ 3,376    │      │ Impute   │      │ 18 algo  │      │ Streamlit│
    │ buildings│      │ Encode   │      │ GridSrch │      │ SHAP     │
    │ 47 vars  │      │ Scale    │      │ 10-fold  │      │ API      │
    └──────────┘      └──────────┘      └──────────┘      └──────────┘
```

### Stack Technique

| Catégorie | Technologies |
|-----------|--------------|
| **Data** | pandas, numpy, scipy |
| **Visualisation** | matplotlib, seaborn, plotly |
| **ML** | scikit-learn, XGBoost |
| **Interprétabilité** | SHAP |
| **Web App** | Streamlit |
| **Versioning** | Git, GitHub |

---

## Résultats & Impact

### Comparaison des Modèles

| Rang | Modèle | RMSE | vs Baseline |
|------|--------|------|-------------|
| 1 | **Random Forest** | **12.9M** | **+45.5%** |
| 2 | Gradient Boosting | 14.3M | +39.6% |
| 3 | AdaBoost | 14.6M | +38.2% |
| 4 | SVR | 15.3M | +35.3% |
| 5 | XGBoost | 15.5M | +34.6% |
| - | Baseline (Mean) | 23.6M | 0% |

### Top 5 Facteurs d'Influence

Les facteurs ayant le plus d'impact sur la consommation :

| # | Feature | Impact | Insight |
|---|---------|--------|---------|
| 1 | **Surface totale** | 42.3% | Plus grand = plus énergivore |
| 2 | **Surface usage principal** | 18.7% | Type d'activité déterminant |
| 3 | **Score efficacité énergétique** | 12.1% | Efficacité = économies |
| 4 | **Âge du bâtiment** | 8.4% | Ancien = moins efficient |
| 5 | **Nombre d'étages** | 5.2% | Hauteur = complexité |

### Impact Business

| Métrique | Avant | Après | Amélioration |
|----------|-------|-------|--------------|
| Temps d'analyse | 2-3 semaines | **< 1 seconde** | **99.9%** |
| Précision prédiction | ±23.6M kBtu | **±12.9M kBtu** | **45%** |
| Facteurs identifiés | 0 | **10 clés** | ∞ |
| Interactivité | PDF statique | **Web app** | ✓ |

---

## Demo Application

### Application Streamlit

**Fonctionnalités** :
- Inputs interactifs (sliders, selects)
- Prédiction temps réel
- Visualisations Plotly
- Recommandations personnalisées

```bash
# Lancer en local
streamlit run app.py
```

---

## Structure du Projet

```
P3-schneider-energy-prediction/
│
├── docs/                          # Documentation projet
│   ├── BRIEF_CLIENT.md           # Brief de mission initial
│   ├── PROPOSITION_TECHNIQUE.md  # Réponse technique
│   ├── RAPPORT_FINAL.md          # Livrable final client
│   └── assets/                   # Images et diagrammes
│
├── notebooks/                     # Travail technique
│   ├── 01_exploration.ipynb      # EDA & Feature Engineering
│   ├── 02_prediction_energy.ipynb # Modélisation énergie
│   └── 03_prediction_co2.ipynb   # Modélisation CO2
│
├── data/                          # Données (version Seattle pour portfolio)
├── models/                        # Modèles sauvegardés
├── app.py                         # Application Streamlit
├── requirements.txt               # Dépendances
└── README.md                      # Ce fichier
```

---

## Défis & Solutions

| Défi | Solution | Résultat |
|------|----------|----------|
| 34% de valeurs manquantes | IterativeImputer (MICE) | Imputation robuste |
| Distribution asymétrique | Transformation log1p | Meilleure performance |
| 47 variables initiales | Feature selection | 40 features pertinentes |
| Interprétabilité exigée | SHAP values | Explications claires |

---

## Installation

### Prérequis

- Python 3.8+
- pip
- Kaggle account (for data download)

### Installation Rapide

```bash
# Cloner le repo
git clone https://github.com/ThomasMeb/schneider-energy-prediction.git
cd schneider-energy-prediction

# Environnement virtuel
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Dépendances
pip install -r requirements.txt
```

### Data Setup

Les données ne sont pas incluses dans le repository. Téléchargez-les depuis Kaggle :

**Option 1 : Script automatique (recommandé)**

```bash
# 1. Configurer l'API Kaggle (une seule fois)
pip install kaggle
# Télécharger kaggle.json depuis https://www.kaggle.com/settings
mkdir -p ~/.kaggle && mv ~/Downloads/kaggle.json ~/.kaggle/
chmod 600 ~/.kaggle/kaggle.json

# 2. Télécharger les données
./scripts/download_data.sh
```

**Option 2 : Téléchargement manuel**

1. Aller sur [Seattle Building Energy Benchmarking](https://www.kaggle.com/datasets/city-of-seattle/sea-building-energy-benchmarking)
2. Télécharger et extraire dans `data/`

### Lancer l'application

```bash
streamlit run app.py
```

---

## Contact

### Thomas Mebarki
**Data Scientist & ML Engineer**

[![GitHub](https://img.shields.io/badge/GitHub-ThomasMeb-181717?style=for-the-badge&logo=github)](https://github.com/ThomasMeb)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Thomas%20Mebarki-0A66C2?style=for-the-badge&logo=linkedin)](https://linkedin.com/in/thomas-mebarki)

---

## Licence

Ce projet est sous licence MIT — voir [LICENSE](LICENSE) pour plus de détails.

---

<p align="center">
  <b>Contribuer à un avenir durable grâce à la Data Science</b>
  <br><br>
  <i>Mission réalisée en Novembre-Décembre 2023</i>
</p>
