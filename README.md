# 🏢 Prédiction des Émissions de CO2 et Consommation Énergétique - Seattle

![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=flat&logo=python&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-1.0+-F7931E?style=flat&logo=scikit-learn&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-1.3+-150458?style=flat&logo=pandas&logoColor=white)
![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-F37626?style=flat&logo=jupyter&logoColor=white)
![XGBoost](https://img.shields.io/badge/XGBoost-1.5+-FF6600?style=flat)
![SHAP](https://img.shields.io/badge/SHAP-Interpretability-00BFFF?style=flat)
![License](https://img.shields.io/badge/License-MIT-green?style=flat)
![Status](https://img.shields.io/badge/Status-Completed-success?style=flat)
![Streamlit](https://img.shields.io/badge/Streamlit-App-FF4B4B?style=flat&logo=streamlit&logoColor=white)

> **🎯 Résumé** : Modèle ML prédisant les émissions CO2 de 1,650 bâtiments de Seattle avec **45% d'amélioration** vs baseline, utilisant Random Forest optimisé et interprétabilité SHAP. Projet réalisé dans le cadre de l'objectif de neutralité carbone 2050 de la ville.

---

## 📑 Table des Matières

- [Demo](#-demo)
- [Contexte](#-contexte)
- [Résultats Clés](#-résultats-clés)
- [Dataset](#-dataset)
- [Méthodologie](#-méthodologie)
- [Structure du Projet](#-structure-du-projet)
- [Installation](#-installation)
- [Compétences Démontrées](#-compétences-démontrées)
- [Auteur](#-auteur)

---

## 🚀 Demo

### Application Streamlit Interactive

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://seattle-co2-predictor.streamlit.app)

Testez le modèle en temps réel avec notre application web :

```bash
# Lancer en local
streamlit run app.py
```

**Fonctionnalités :**
- 🏢 Saisie des caractéristiques du bâtiment
- 🔋 Prédiction de la consommation énergétique
- 🌿 Estimation des émissions CO2
- 📊 Visualisation de l'impact des facteurs
- 💡 Recommandations personnalisées

![App Screenshot](docs/app_screenshot.png)

---

## 🌍 Contexte

La ville de Seattle s'est fixé l'objectif ambitieux d'atteindre la **neutralité carbone d'ici 2050**. Ce projet développe des modèles de Machine Learning pour :

- 🔋 **Prédire la consommation énergétique** des bâtiments non résidentiels
- 🌿 **Prédire les émissions de CO2** (gaz à effet de serre)
- 🔍 **Identifier les facteurs clés** influençant ces métriques
- 💡 **Fournir des recommandations** pour la stratégie de réduction des émissions

---

## 🏆 Résultats Clés

| Métrique | Valeur |
|----------|--------|
| **Meilleur modèle** | Random Forest |
| **RMSE** | 12,877,388 kBtu |
| **Amélioration vs Baseline** | **45.5%** |
| **Modèles testés** | 18 |
| **Cross-validation** | 10-fold |

### Top 5 Features les Plus Importantes

1. 📐 **PropertyGFATotal** — Surface totale du bâtiment
2. 🏗️ **LargestPropertyUseTypeGFA** — Surface de l'usage principal
3. ⭐ **ENERGYSTARScore** — Score de performance énergétique
4. 📅 **Age** — Âge du bâtiment
5. 🏢 **NumberofFloors** — Nombre d'étages

### Comparaison des Modèles

| Rang | Modèle | RMSE | Amélioration |
|------|--------|------|--------------|
| 🥇 | **Random Forest** | 12,877,388 | +45.5% |
| 🥈 | Gradient Boosting (TT) | 14,282,043 | +39.6% |
| 🥉 | AdaBoost | 14,605,126 | +38.2% |
| 4 | SVR (TT) | 15,288,219 | +35.3% |
| 5 | XGBoost (TT) | 15,457,243 | +34.6% |
| ... | Baseline (Mean) | 23,631,178 | 0% |

*TT = TransformedTargetRegressor avec log1p*

---

## 📊 Dataset

**Source** : [Seattle 2016 Building Energy Benchmarking](https://data.seattle.gov/dataset/2016-Building-Energy-Benchmarking/2bpz-gwpy)

| Caractéristique | Valeur |
|-----------------|--------|
| **Période** | 2016 |
| **Observations** | ~1,650 bâtiments (après nettoyage) |
| **Features** | 40+ variables |
| **Scope** | Bâtiments non résidentiels |

**Types de variables** :
- Structurelles : surface, étages, âge
- Énergétiques : consommation électricité, gaz, vapeur
- Performance : Score ENERGY STAR
- Localisation : district municipal

---

## 🔬 Méthodologie

### Pipeline ML Complet

```
┌─────────────┐    ┌─────────────┐    ┌─────────────┐    ┌─────────────┐
│     EDA     │ -> │ Preprocessing│ -> │ Modélisation│ -> │   SHAP      │
│             │    │             │    │             │    │             │
│ • Distrib.  │    │ • Imputation│    │ • 18 modèles│    │ • Feature   │
│ • Outliers  │    │ • Encoding  │    │ • GridSearch│    │   Importance│
│ • Corrélat. │    │ • Scaling   │    │ • 10-fold CV│    │ • Force Plot│
└─────────────┘    └─────────────┘    └─────────────┘    └─────────────┘
```

### Notebooks

| # | Notebook | Description |
|---|----------|-------------|
| 1 | `01_exploration.ipynb` | EDA, feature engineering, nettoyage |
| 2 | `02_prediction_energy.ipynb` | Modélisation consommation énergétique |
| 3 | `03_prediction_co2.ipynb` | Modélisation émissions CO2 |

### Techniques Utilisées

- **Imputation** : IterativeImputer (MICE)
- **Encoding** : One-Hot Encoding
- **Scaling** : StandardScaler
- **Transformation** : log1p pour features asymétriques
- **Optimisation** : GridSearchCV avec validation croisée
- **Interprétabilité** : SHAP values

---

## 📁 Structure du Projet

```
Anticiper_besoins_des_batiments/
│
├── 📂 data/
│   ├── 2016_Building_Energy_Benchmarking.csv   # Données brutes
│   └── data_cleaned.csv                        # Données nettoyées
│
├── 📂 notebooks/
│   ├── 01_exploration.ipynb                    # EDA & Feature Engineering
│   ├── 02_prediction_energy.ipynb              # Modèles consommation
│   └── 03_prediction_co2.ipynb                 # Modèles émissions CO2
│
├── 📂 models/                                  # Modèles sauvegardés
│   └── random_forest_best.pkl                  # Meilleur modèle
│
├── 📄 app.py                                   # 🚀 Application Streamlit
├── 📄 README.md                                # Ce fichier
├── 📄 requirements.txt                         # Dépendances Python
├── 📄 LICENSE                                  # Licence MIT
└── 📄 .gitignore                               # Fichiers ignorés
```

---

## 🚀 Installation

### Prérequis

- Python 3.8+
- pip

### Installation rapide

```bash
# Cloner le repository
git clone https://github.com/ThomasMeb/Anticiper_besoins_des_batiments.git
cd Anticiper_besoins_des_batiments

# Créer environnement virtuel
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Installer dépendances
pip install -r requirements.txt

# Lancer Jupyter
jupyter notebook
```

### Ordre d'exécution des notebooks

1. `notebooks/01_exploration.ipynb`
2. `notebooks/02_prediction_energy.ipynb`
3. `notebooks/03_prediction_co2.ipynb`

---

## 💼 Compétences Démontrées

| Domaine | Compétences |
|---------|-------------|
| **Data Science** | EDA, feature engineering, data cleaning |
| **Machine Learning** | Régression, ensembles, hyperparameter tuning |
| **Preprocessing** | Imputation MICE, encoding, scaling |
| **Évaluation** | Cross-validation, métriques multiples |
| **Interprétabilité** | SHAP values, feature importance |
| **Python** | pandas, scikit-learn, XGBoost, matplotlib |

---

## 🔮 Améliorations Futures

- [x] ~~Dashboard interactif (Streamlit)~~ ✅
- [ ] Déploiement sur Streamlit Cloud
- [ ] API REST pour prédictions en temps réel
- [ ] Intégration données météorologiques
- [ ] Analyse géospatiale par quartier
- [ ] Séries temporelles (données multi-années)

---

## 👤 Auteur

**Thomas Mebarki**

[![GitHub](https://img.shields.io/badge/GitHub-ThomasMeb-181717?style=flat&logo=github)](https://github.com/ThomasMeb)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Thomas%20Mebarki-0A66C2?style=flat&logo=linkedin)](https://www.linkedin.com/in/thomas-mebarki/)

---

## 📜 Licence

Ce projet est sous licence MIT - voir le fichier [LICENSE](LICENSE) pour plus de détails.

---

## 🙏 Remerciements

- **Ville de Seattle** pour la mise à disposition des données open data
- **OpenClassrooms** pour l'encadrement pédagogique

---

<p align="center">
  <i>Dernière mise à jour : Janvier 2024</i>
</p>
