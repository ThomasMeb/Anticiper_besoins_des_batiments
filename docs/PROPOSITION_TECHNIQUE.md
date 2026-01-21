# 📑 Proposition Technique — Mission Seattle Energy Intelligence

> **Réponse à l'appel d'offres** — Ville de Seattle
> **Prestataire** : Thomas Mebarki — Data Scientist Freelance
> **Date** : 20 Octobre 2023

---

## 👤 Présentation du Prestataire

**Thomas Mebarki**
Data Scientist & Machine Learning Engineer

| Compétence | Niveau |
|------------|--------|
| Python / Data Science | ⭐⭐⭐⭐⭐ |
| Machine Learning | ⭐⭐⭐⭐⭐ |
| Visualisation de données | ⭐⭐⭐⭐ |
| Communication client | ⭐⭐⭐⭐ |

**Contact** :
- GitHub : [ThomasMeb](https://github.com/ThomasMeb)
- LinkedIn : [Thomas Mebarki](https://linkedin.com/in/thomas-mebarki)

---

## 🎯 Compréhension de la Mission

### Enjeux Identifiés

1. **Enjeu climatique** : Atteindre la neutralité carbone 2050
2. **Enjeu opérationnel** : Automatiser l'analyse des bâtiments
3. **Enjeu décisionnel** : Prioriser les investissements de rénovation
4. **Enjeu politique** : Mesurer l'efficacité des politiques publiques

### Valeur Ajoutée Proposée

| Problème Actuel | Solution Proposée |
|-----------------|-------------------|
| Analyse manuelle (2-3 semaines) | Prédiction instantanée (<1 seconde) |
| Basé sur moyennes historiques | Modèle ML personnalisé |
| Pas d'identification des facteurs | Feature importance + SHAP |
| Rapports statiques | Dashboard interactif |

---

## 🔬 Approche Méthodologique

### Phase 1 : Cadrage & Exploration (Semaine 1)

**Objectifs** :
- Validation du brief avec le client
- Compréhension approfondie des données
- Définition des KPIs de succès

**Activités** :
- [ ] Kick-off meeting avec l'équipe Seattle
- [ ] Analyse exploratoire préliminaire (EDA)
- [ ] Identification des variables clés
- [ ] Validation du périmètre

**Livrable** : Rapport d'exploration préliminaire

---

### Phase 2 : Analyse Approfondie (Semaine 2)

**Objectifs** :
- Nettoyage et préparation des données
- Feature engineering
- Analyse des corrélations et patterns

**Activités** :
- [ ] Traitement des valeurs manquantes (IterativeImputer)
- [ ] Détection et gestion des outliers
- [ ] Création de nouvelles features (Age, ratios, %)
- [ ] Encodage des variables catégorielles
- [ ] Normalisation et transformations

**Livrable** : Dataset nettoyé + Rapport d'analyse

---

### Phase 3 : Modélisation (Semaine 3)

**Objectifs** :
- Développement et comparaison de modèles
- Optimisation des hyperparamètres
- Validation de la performance

**Modèles Prévus** :

| Catégorie | Modèles |
|-----------|---------|
| Baseline | DummyRegressor (moyenne) |
| Linéaires | Linear Regression, Ridge, Lasso |
| SVM | SVR (RBF, Poly) |
| Ensembles | Random Forest, Gradient Boosting, AdaBoost |
| Boosting | XGBoost |
| Neural | MLP Regressor |

**Méthodologie d'évaluation** :
- Validation croisée 10-fold
- Métriques : RMSE, MAE, R²
- GridSearchCV pour l'optimisation

**Livrable** : Modèles entraînés + Rapport comparatif

---

### Phase 4 : Livraison (Semaine 4)

**Objectifs** :
- Interprétabilité des résultats
- Développement de l'interface utilisateur
- Documentation et transfert de connaissances

**Activités** :
- [ ] Analyse SHAP pour l'interprétabilité
- [ ] Développement application Streamlit
- [ ] Rédaction documentation technique
- [ ] Préparation soutenance client

**Livrables** :
- Application web de prédiction
- Rapport final
- Code source documenté
- Présentation de soutenance

---

## 🛠️ Stack Technique

### Langages & Frameworks

```
┌─────────────────────────────────────────────────────────────┐
│                        STACK TECHNIQUE                       │
├─────────────────────────────────────────────────────────────┤
│  📊 Data Manipulation    │  pandas, numpy                   │
├──────────────────────────┼──────────────────────────────────┤
│  📈 Visualisation        │  matplotlib, seaborn, plotly     │
├──────────────────────────┼──────────────────────────────────┤
│  🤖 Machine Learning     │  scikit-learn, XGBoost           │
├──────────────────────────┼──────────────────────────────────┤
│  🔍 Interprétabilité     │  SHAP                            │
├──────────────────────────┼──────────────────────────────────┤
│  🌐 Web App              │  Streamlit                       │
├──────────────────────────┼──────────────────────────────────┤
│  📦 Environnement        │  Python 3.8+, Jupyter, Git       │
└──────────────────────────┴──────────────────────────────────┘
```

### Architecture Solution

```
┌──────────────┐     ┌──────────────┐     ┌──────────────┐
│   DONNÉES    │     │   MODÈLE     │     │   SORTIE     │
│              │     │              │     │              │
│ • CSV brut   │ --> │ • Cleaning   │ --> │ • Prédiction │
│ • 3,400 obs  │     │ • Training   │     │ • Dashboard  │
│ • 47 vars    │     │ • Tuning     │     │ • Rapport    │
└──────────────┘     └──────────────┘     └──────────────┘
```

---

## 📊 Critères de Succès

### KPIs Quantitatifs

| Métrique | Objectif | Mesure |
|----------|----------|--------|
| **RMSE** | -30% vs baseline | Validation croisée |
| **R²** | > 0.7 | Test set |
| **Couverture** | 100% bâtiments | Prédiction possible |
| **Temps prédiction** | < 1 seconde | Benchmark |

### KPIs Qualitatifs

| Critère | Objectif |
|---------|----------|
| **Interprétabilité** | Top 10 features explicables |
| **Utilisabilité** | Interface intuitive (non-tech) |
| **Documentation** | Autonomie du client |
| **Maintenabilité** | Code modulaire et testé |

---

## 📅 Planning Détaillé

```
OCTOBRE 2023
──────────────────────────────────────────────────────────────
Semaine 1 (23-27 Oct)  │████████████████████│ Cadrage & EDA
Semaine 2 (30-03 Nov)  │████████████████████│ Analyse & Cleaning
Semaine 3 (06-10 Nov)  │████████████████████│ Modélisation
Semaine 4 (13-17 Nov)  │████████████████████│ Livraison
──────────────────────────────────────────────────────────────
                        ▲                    ▲
                     Revue                Soutenance
                   mi-parcours             finale
```

### Points de Synchronisation

| Date | Événement | Format |
|------|-----------|--------|
| 23 Oct | Kick-off | Visio 1h |
| 03 Nov | Revue mi-parcours | Visio 30min |
| 10 Nov | Démo modèle | Visio 30min |
| 17 Nov | Soutenance finale | Visio 1h |

---

## 🔒 Engagements

### Confidentialité
- Données traitées uniquement pour cette mission
- Suppression des données à la fin du projet
- NDA signé si requis

### Propriété Intellectuelle
- Code source livré au client
- Licence MIT pour réutilisation interne
- Pas de publication sans accord

### Support Post-Livraison
- 2 semaines de support inclus
- Corrections de bugs gratuits
- Formation utilisateur (1h)

---

## ✅ Conclusion

Cette proposition répond aux objectifs de la Ville de Seattle en apportant :

1. **Expertise technique** éprouvée en ML et Data Science
2. **Méthodologie rigoureuse** (CRISP-DM adapté)
3. **Livrables concrets** et utilisables immédiatement
4. **Valeur business** mesurable (45%+ d'amélioration attendue)

Je suis convaincu que cette collaboration permettra à Seattle de franchir une étape décisive vers ses objectifs de neutralité carbone.

---

**Thomas Mebarki**
Data Scientist Freelance

*Proposition valable jusqu'au 30 Octobre 2023*
