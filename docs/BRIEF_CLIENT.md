# 📋 Brief de Mission — Ville de Seattle

> **Document confidentiel** — Appel d'offres pour prestation de Data Science

---

## 🏛️ Présentation du Client

**Client** : Seattle Office of Sustainability & Environment (OSE)
**Contact** : Direction de la Planification Urbaine
**Secteur** : Administration publique — Développement durable
**Localisation** : Seattle, Washington, USA

---

## 🌍 Contexte

La Ville de Seattle s'est engagée dans un **plan ambitieux de neutralité carbone d'ici 2050**, conformément à l'Accord de Paris et aux objectifs de l'État de Washington.

Les bâtiments représentent **33% des émissions de gaz à effet de serre** de la ville. Pour atteindre nos objectifs climatiques, nous devons :

1. Identifier les bâtiments les plus énergivores
2. Prioriser les actions de rénovation énergétique
3. Anticiper l'impact des nouvelles constructions
4. Mesurer l'efficacité de nos politiques environnementales

**Problème actuel** : Nous disposons de données de benchmarking énergétique pour ~3,000 bâtiments, mais l'analyse manuelle est :
- Chronophage (2-3 semaines par rapport)
- Peu prédictive (basée sur des moyennes historiques)
- Incapable d'identifier les facteurs clés d'optimisation

---

## 🎯 Objectif de la Mission

### Objectif Principal

Développer un **outil de prédiction** capable d'estimer la consommation énergétique et les émissions CO2 des bâtiments non résidentiels à partir de leurs caractéristiques structurelles.

### Objectifs SMART

| Critère | Objectif |
|---------|----------|
| **Spécifique** | Modèle ML prédisant `SiteEnergyUse` et `TotalGHGEmissions` |
| **Mesurable** | Erreur de prédiction (RMSE) inférieure de 30% au baseline |
| **Atteignable** | Utilisation des données existantes (2016 Benchmarking) |
| **Réaliste** | Stack Python/scikit-learn, technologies éprouvées |
| **Temporel** | Livraison sous 4 semaines |

### Questions Clés à Résoudre

1. Quels facteurs influencent le plus la consommation énergétique ?
2. Peut-on prédire les émissions sans relevés de consommation ?
3. Quels types de bâtiments prioriser pour les rénovations ?
4. Quel est l'impact du score ENERGY STAR sur les prédictions ?

---

## 📊 Données Disponibles

### Dataset Principal

**Source** : [Seattle Open Data — 2016 Building Energy Benchmarking](https://data.seattle.gov/dataset/2016-Building-Energy-Benchmarking/2bpz-gwpy)

| Caractéristique | Valeur |
|-----------------|--------|
| **Observations** | ~3,400 bâtiments |
| **Variables** | 47 colonnes |
| **Période** | 2016 |
| **Format** | CSV |

### Variables Clés

**Structurelles** :
- Surface totale (PropertyGFATotal)
- Nombre d'étages (NumberofFloors)
- Année de construction (YearBuilt)
- Type de propriété (PrimaryPropertyType)

**Énergétiques** :
- Consommation totale (SiteEnergyUse)
- Électricité, Gaz naturel, Vapeur
- Score ENERGY STAR

**Environnementales** :
- Émissions GES (TotalGHGEmissions)
- Intensité des émissions (GHGEmissionsIntensity)

---

## 📦 Livrables Attendus

### 1. Modèle Prédictif
- Modèle entraîné et optimisé
- Documentation des hyperparamètres
- Métriques de performance validées

### 2. Analyse Exploratoire
- Rapport d'analyse des données
- Visualisations des distributions et corrélations
- Identification des outliers et anomalies

### 3. Outil de Prédiction
- Interface utilisateur (web ou notebook)
- Possibilité de saisir les caractéristiques d'un bâtiment
- Prédiction instantanée avec intervalle de confiance

### 4. Recommandations
- Top 10 des facteurs d'influence
- Stratégies de réduction des émissions
- Bâtiments prioritaires pour rénovation

### 5. Documentation
- Code source commenté
- Guide d'utilisation
- Rapport technique final

---

## 📅 Planning Prévisionnel

| Semaine | Phase | Livrables |
|---------|-------|-----------|
| **S1** | Cadrage & Exploration | Brief validé, EDA préliminaire |
| **S2** | Analyse approfondie | Rapport EDA, données nettoyées |
| **S3** | Modélisation | Modèles entraînés, comparatifs |
| **S4** | Livraison | Outil final, documentation, soutenance |

---

## 💰 Budget & Conditions

| Élément | Détail |
|---------|--------|
| **Type de contrat** | Prestation freelance |
| **Durée** | 4 semaines |
| **Mode de travail** | Remote |
| **Réunions** | 1x/semaine (visio) |
| **Propriété intellectuelle** | Cession totale au client |

---

## ✅ Critères de Sélection

Le prestataire sera évalué sur :

1. **Expertise technique** — Maîtrise ML, Python, Data Science
2. **Compréhension métier** — Sensibilité aux enjeux environnementaux
3. **Communication** — Capacité à vulgariser les résultats
4. **Portfolio** — Projets similaires réalisés
5. **Disponibilité** — Respect des délais

---

## 📞 Contact

Pour toute question concernant cet appel d'offres :

**Seattle Office of Sustainability & Environment**
700 5th Avenue, Suite 2748
Seattle, WA 98104

---

*Document émis le 15 Octobre 2023*
*Date limite de réponse : 22 Octobre 2023*
