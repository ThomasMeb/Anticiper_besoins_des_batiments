# 🏢 Seattle Energy Intelligence

### Mission Freelance — Prédiction Énergétique pour la Ville de Seattle

![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-1.0+-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-App-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

<p align="center">
  <img src="docs/assets/banner.jpg" alt="Seattle Skyline" width="800">
</p>

> **🎯 Mission** : Développer un outil ML prédisant la consommation énergétique et les émissions CO2 des bâtiments non résidentiels de Seattle, dans le cadre de l'objectif de **neutralité carbone 2050**.

---

## 📋 Résumé Exécutif

| Élément | Détail |
|---------|--------|
| **Client** | Ville de Seattle — Office of Sustainability & Environment |
| **Durée** | 4 semaines (Oct-Nov 2023) |
| **Objectif** | Prédire consommation énergétique avec >30% d'amélioration vs baseline |
| **Résultat** | **45.5% d'amélioration** — Objectif dépassé ✅ |
| **Livrable** | Modèle ML + Application Web + Documentation |

### 🏆 Résultats Clés

```
┌────────────────────────────────────────────────────────────────┐
│                     PERFORMANCE DU MODÈLE                       │
├────────────────────────────────────────────────────────────────┤
│                                                                │
│   📊 Amélioration vs Baseline    ████████████████████░  45.5%  │
│                                                                │
│   🎯 Objectif Initial            ████████████░░░░░░░░░  30%    │
│                                                                │
│   ✅ Résultat : OBJECTIF DÉPASSÉ DE +15.5 POINTS               │
│                                                                │
└────────────────────────────────────────────────────────────────┘
```

---

## 📑 Table des Matières

1. [Contexte & Problématique](#-contexte--problématique)
2. [Objectifs SMART](#-objectifs-smart)
3. [Approche & Méthodologie](#-approche--méthodologie)
4. [Résultats & Impact](#-résultats--impact)
5. [Demo Application](#-demo-application)
6. [Livrables](#-livrables)
7. [Retour d'Expérience](#-retour-dexpérience)
8. [Installation](#-installation)
9. [Contact](#-contact)

---

## 🌍 Contexte & Problématique

### Le Client

La **Ville de Seattle** s'est engagée dans un plan ambitieux de **neutralité carbone d'ici 2050**. Les bâtiments représentent **33% des émissions** de gaz à effet de serre de la ville.

### La Problématique

L'Office of Sustainability & Environment disposait de données sur ~3,000 bâtiments mais faisait face à plusieurs défis :

| Problème | Impact |
|----------|--------|
| Analyse manuelle | 2-3 semaines par rapport |
| Méthode statistique basique | Prédictions peu fiables |
| Pas d'identification des facteurs | Impossible de prioriser les actions |
| Rapports statiques | Pas d'interactivité pour les décideurs |

### La Solution Proposée

Développer un **outil de Machine Learning** capable de :
- ⚡ Prédire instantanément (<1 seconde)
- 🎯 Identifier les facteurs clés d'influence
- 📊 Fournir une interface interactive
- 💡 Générer des recommandations actionnables

---

## 🎯 Objectifs SMART

| Critère | Objectif Défini | Résultat |
|---------|-----------------|----------|
| **S**pécifique | Prédire `SiteEnergyUse` et `TotalGHGEmissions` à partir des caractéristiques structurelles | ✅ 2 modèles développés |
| **M**esurable | RMSE inférieur de 30% au baseline (moyenne) | ✅ **45.5%** d'amélioration |
| **A**tteignable | Utiliser les données 2016 Building Benchmarking | ✅ 1,650 bâtiments analysés |
| **R**éaliste | Stack Python/scikit-learn éprouvé | ✅ 18 modèles comparés |
| **T**emporel | Livraison sous 4 semaines | ✅ Livré dans les délais |

---

## 🔬 Approche & Méthodologie

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
        │          │ • Soutenance client

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
         │                 │                 │                 │
         ▼                 ▼                 ▼                 ▼
    ┌──────────┐      ┌──────────┐      ┌──────────┐      ┌──────────┐
    │ Seattle  │      │ 1,650    │      │ Random   │      │ Web App  │
    │ Open Data│      │ cleaned  │      │ Forest   │      │ Live!    │
    │ CSV      │      │ records  │      │ Winner   │      │          │
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

## 📊 Résultats & Impact

### Comparaison des Modèles

| Rang | Modèle | RMSE | vs Baseline |
|------|--------|------|-------------|
| 🥇 | **Random Forest** | **12.9M** | **+45.5%** |
| 🥈 | Gradient Boosting (TT) | 14.3M | +39.6% |
| 🥉 | AdaBoost | 14.6M | +38.2% |
| 4 | SVR (TT) | 15.3M | +35.3% |
| 5 | XGBoost (TT) | 15.5M | +34.6% |
| ... | ... | ... | ... |
| - | Baseline (Mean) | 23.6M | 0% |

### Top 5 Features

Les facteurs ayant le plus d'impact sur la consommation :

| # | Feature | Impact | Insight |
|---|---------|--------|---------|
| 1 | 📐 **Surface totale** | 42.3% | Plus grand = plus énergivore |
| 2 | 🏗️ **Surface usage principal** | 18.7% | Type d'activité déterminant |
| 3 | ⭐ **Score ENERGY STAR** | 12.1% | Efficacité = économies |
| 4 | 📅 **Âge du bâtiment** | 8.4% | Ancien = moins efficient |
| 5 | 🏢 **Nombre d'étages** | 5.2% | Hauteur = complexité |

### Impact Business

| Métrique | Avant | Après | Amélioration |
|----------|-------|-------|--------------|
| Temps d'analyse | 2-3 semaines | **< 1 seconde** | **99.9%** |
| Précision prédiction | ±23.6M kBtu | **±12.9M kBtu** | **45%** |
| Facteurs identifiés | 0 | **10 clés** | ∞ |
| Interactivité | PDF statique | **Web app** | ✅ |

---

## 🚀 Demo Application

### Application Streamlit

[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://anticiperbesoinsdesbatiments-caxqew8gtaanhb2dtpztzm.streamlit.app/)

**Fonctionnalités** :
- 🎛️ Inputs interactifs (sliders, selects)
- 📊 Prédiction temps réel
- 📈 Visualisations Plotly
- 💡 Recommandations personnalisées

```bash
# Lancer en local
streamlit run app.py
```

### Aperçu

<p align="center">
  <img src="docs/assets/app_screenshot.png" alt="App Screenshot" width="700">
</p>

---

## 📦 Livrables

### Structure du Projet

```
Seattle-Energy-Intelligence/
│
├── 📂 docs/                          # 📋 Documentation projet
│   ├── BRIEF_CLIENT.md              # Brief de mission initial
│   ├── PROPOSITION_TECHNIQUE.md     # Réponse technique
│   ├── RAPPORT_FINAL.md             # Livrable final client
│   └── assets/                      # Images et diagrammes
│
├── 📂 notebooks/                     # 🔬 Travail technique
│   ├── 01_exploration.ipynb         # EDA & Feature Engineering
│   ├── 02_prediction_energy.ipynb   # Modélisation énergie
│   └── 03_prediction_co2.ipynb      # Modélisation CO2
│
├── 📂 data/                          # 📊 Données
│   └── 2016_Building_Energy_Benchmarking.csv
│
├── 📂 models/                        # 🤖 Modèles sauvegardés
│
├── 📄 app.py                         # 🚀 Application Streamlit
├── 📄 requirements.txt               # 📦 Dépendances
├── 📄 LICENSE                        # ⚖️ Licence MIT
└── 📄 README.md                      # 📖 Ce fichier
```

### Documents de Mission

| Document | Description | Lien |
|----------|-------------|------|
| 📋 Brief Client | Cahier des charges initial | [BRIEF_CLIENT.md](docs/BRIEF_CLIENT.md) |
| 📑 Proposition | Réponse technique au brief | [PROPOSITION_TECHNIQUE.md](docs/PROPOSITION_TECHNIQUE.md) |
| 📊 Rapport Final | Livrable de fin de mission | [RAPPORT_FINAL.md](docs/RAPPORT_FINAL.md) |

---

## 💡 Retour d'Expérience

### Défis Rencontrés & Solutions

| Défi | Solution | Résultat |
|------|----------|----------|
| 34% de valeurs manquantes (ENERGY STAR) | IterativeImputer (MICE) | Imputation robuste |
| Distribution très asymétrique | Transformation log1p | Meilleure performance |
| 47 variables initiales | Feature selection + engineering | 40 features pertinentes |
| Interprétabilité exigée | SHAP values | Explications claires |

### Compétences Mobilisées

| Domaine | Compétences |
|---------|-------------|
| **Data Science** | EDA, feature engineering, data cleaning |
| **Machine Learning** | Régression, ensembles, hyperparameter tuning |
| **MLOps** | Pipeline, validation croisée, métriques |
| **Visualisation** | matplotlib, seaborn, plotly, SHAP |
| **Web Dev** | Streamlit, déploiement cloud |
| **Communication** | Rapports, présentations, vulgarisation |

### Leçons Apprises

1. **L'EDA est cruciale** — 2 jours d'exploration = 2 semaines gagnées
2. **Baseline first** — Toujours mesurer vs un modèle naïf
3. **Feature engineering > model tuning** — Les bonnes features font 80% du travail
4. **Interprétabilité = valeur** — SHAP a convaincu le client plus que le RMSE

---

## 🛠️ Installation

### Prérequis

- Python 3.8+
- pip

### Installation Rapide

```bash
# Cloner le repo
git clone https://github.com/ThomasMeb/Anticiper_besoins_des_batiments.git
cd Anticiper_besoins_des_batiments

# Environnement virtuel
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Dépendances
pip install -r requirements.txt

# Lancer l'app
streamlit run app.py
```

### Exécuter les Notebooks

```bash
jupyter notebook
# Ouvrir dans l'ordre : 01 → 02 → 03
```

---

## 👤 Contact

### Thomas Mebarki
**Data Scientist & ML Engineer**

[![GitHub](https://img.shields.io/badge/GitHub-ThomasMeb-181717?style=for-the-badge&logo=github)](https://github.com/ThomasMeb)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Thomas%20Mebarki-0A66C2?style=for-the-badge&logo=linkedin)](https://linkedin.com/in/thomas-mebarki)

---

## 📜 Licence

Ce projet est sous licence MIT — voir [LICENSE](LICENSE) pour plus de détails.

---

<p align="center">
  <b>🌿 Contribuer à un avenir durable grâce à la Data Science</b>
  <br><br>
  <i>Projet réalisé en Novembre 2023</i>
</p>
