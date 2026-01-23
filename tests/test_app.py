"""
Tests pour l'application Seattle Energy Predictor.
"""

import pytest
import pandas as pd
import numpy as np
from pathlib import Path
import joblib
import sys

sys.path.insert(0, str(Path(__file__).parent.parent))


class TestModelsLoading:
    """Tests pour le chargement des modèles."""

    def test_energy_model_exists(self, models_path):
        """Vérifie que le modèle énergie existe."""
        assert (models_path / "energy_model.joblib").exists()

    def test_co2_model_exists(self, models_path):
        """Vérifie que le modèle CO2 existe."""
        assert (models_path / "co2_model.joblib").exists()

    def test_energy_scaler_exists(self, models_path):
        """Vérifie que le scaler énergie existe."""
        assert (models_path / "energy_scaler.joblib").exists()

    def test_co2_scaler_exists(self, models_path):
        """Vérifie que le scaler CO2 existe."""
        assert (models_path / "co2_scaler.joblib").exists()

    def test_energy_features_exists(self, models_path):
        """Vérifie que les features énergie existent."""
        assert (models_path / "energy_features.joblib").exists()

    def test_load_energy_model(self, models_path):
        """Vérifie que le modèle énergie se charge correctement."""
        model = joblib.load(models_path / "energy_model.joblib")
        assert hasattr(model, 'predict')
        assert hasattr(model, 'feature_importances_')

    def test_load_co2_model(self, models_path):
        """Vérifie que le modèle CO2 se charge correctement."""
        model = joblib.load(models_path / "co2_model.joblib")
        assert hasattr(model, 'predict')


class TestPrepareFeatures:
    """Tests pour la préparation des features."""

    def test_prepare_features_returns_dataframe(self, sample_features, feature_names):
        """Vérifie que prepare_features retourne un DataFrame."""
        from app import prepare_features

        df = prepare_features(
            sample_features['property_gfa'],
            sample_features['floors'],
            sample_features['age'],
            sample_features['energy_star'],
            sample_features['building_type'],
            feature_names
        )

        assert isinstance(df, pd.DataFrame)
        assert len(df) == 1

    def test_prepare_features_correct_columns(self, sample_features, feature_names):
        """Vérifie que les colonnes sont dans le bon ordre."""
        from app import prepare_features

        df = prepare_features(
            sample_features['property_gfa'],
            sample_features['floors'],
            sample_features['age'],
            sample_features['energy_star'],
            sample_features['building_type'],
            feature_names
        )

        assert list(df.columns) == feature_names

    def test_prepare_features_correct_values(self, sample_features, feature_names):
        """Vérifie que les valeurs sont correctement assignées."""
        from app import prepare_features

        df = prepare_features(
            sample_features['property_gfa'],
            sample_features['floors'],
            sample_features['age'],
            sample_features['energy_star'],
            sample_features['building_type'],
            feature_names
        )

        assert df['Age'].iloc[0] == sample_features['age']
        assert df['NumberofFloors'].iloc[0] == sample_features['floors']
        assert df['PropertyGFATotal'].iloc[0] == sample_features['property_gfa']
        assert df['ENERGYSTARScore'].iloc[0] == sample_features['energy_star']

    def test_prepare_features_building_type_encoding(self, feature_names):
        """Vérifie l'encodage one-hot du type de bâtiment."""
        from app import prepare_features

        df = prepare_features(50000, 5, 30, 50, 'Hotel', feature_names)

        assert df['PropType_Hotel'].iloc[0] == 1
        assert df['PropType_Large Office'].iloc[0] == 0


class TestPredictions:
    """Tests pour les prédictions."""

    def test_energy_prediction_positive(self, models_path, sample_features, feature_names):
        """Vérifie que la prédiction d'énergie est positive."""
        from app import prepare_features

        model = joblib.load(models_path / "energy_model.joblib")
        scaler = joblib.load(models_path / "energy_scaler.joblib")
        features = joblib.load(models_path / "energy_features.joblib")

        X = prepare_features(
            sample_features['property_gfa'],
            sample_features['floors'],
            sample_features['age'],
            sample_features['energy_star'],
            sample_features['building_type'],
            features
        )

        X_scaled = scaler.transform(X)
        prediction = model.predict(X_scaled)[0]

        assert prediction > 0

    def test_co2_prediction_positive(self, models_path, sample_features, feature_names):
        """Vérifie que la prédiction CO2 est positive."""
        from app import prepare_features

        model = joblib.load(models_path / "co2_model.joblib")
        scaler = joblib.load(models_path / "co2_scaler.joblib")
        features = joblib.load(models_path / "energy_features.joblib")

        X = prepare_features(
            sample_features['property_gfa'],
            sample_features['floors'],
            sample_features['age'],
            sample_features['energy_star'],
            sample_features['building_type'],
            features
        )

        X_scaled = scaler.transform(X)
        prediction = model.predict(X_scaled)[0]

        assert prediction > 0

    def test_larger_building_more_energy(self, models_path):
        """Vérifie qu'un bâtiment plus grand consomme plus d'énergie."""
        from app import prepare_features

        model = joblib.load(models_path / "energy_model.joblib")
        scaler = joblib.load(models_path / "energy_scaler.joblib")
        features = joblib.load(models_path / "energy_features.joblib")

        # Petit bâtiment
        X_small = prepare_features(10000, 2, 30, 50, 'Office (Small/Mid)', features)
        pred_small = model.predict(scaler.transform(X_small))[0]

        # Grand bâtiment
        X_large = prepare_features(100000, 10, 30, 50, 'Office (Small/Mid)', features)
        pred_large = model.predict(scaler.transform(X_large))[0]

        assert pred_large > pred_small


class TestFeatureImportance:
    """Tests pour l'importance des features."""

    def test_feature_importance_sums_to_one(self, models_path):
        """Vérifie que les importances somment à 1."""
        model = joblib.load(models_path / "energy_model.joblib")
        total = sum(model.feature_importances_)
        assert abs(total - 1.0) < 0.01

    def test_gfa_is_important_feature(self, models_path):
        """Vérifie que la surface est une feature importante."""
        model = joblib.load(models_path / "energy_model.joblib")
        features = joblib.load(models_path / "energy_features.joblib")

        importance_df = pd.DataFrame({
            'Feature': features,
            'Importance': model.feature_importances_
        }).sort_values('Importance', ascending=False)

        top_features = importance_df.head(3)['Feature'].tolist()

        # PropertyGFATotal ou LargestPropertyUseTypeGFA devrait être dans le top 3
        gfa_features = ['PropertyGFATotal', 'LargestPropertyUseTypeGFA']
        assert any(f in top_features for f in gfa_features)


class TestLoadModels:
    """Tests pour la fonction load_models."""

    def test_load_models_returns_dict(self, monkeypatch):
        """Vérifie que load_models retourne un dictionnaire."""
        # Change le répertoire de travail vers Projet_3
        import os
        monkeypatch.chdir(Path(__file__).parent.parent)

        from app import load_models
        # Clear le cache Streamlit pour forcer le rechargement
        load_models.clear()
        models = load_models()

        assert models is not None
        assert isinstance(models, dict)

    def test_load_models_contains_energy_model(self, monkeypatch):
        """Vérifie que le dictionnaire contient le modèle énergie."""
        import os
        monkeypatch.chdir(Path(__file__).parent.parent)

        from app import load_models
        load_models.clear()
        models = load_models()

        assert 'energy_model' in models
        assert hasattr(models['energy_model'], 'predict')

    def test_load_models_contains_co2_model(self, monkeypatch):
        """Vérifie que le dictionnaire contient le modèle CO2."""
        import os
        monkeypatch.chdir(Path(__file__).parent.parent)

        from app import load_models
        load_models.clear()
        models = load_models()

        assert 'co2_model' in models
        assert hasattr(models['co2_model'], 'predict')

    def test_load_models_contains_scalers(self, monkeypatch):
        """Vérifie que le dictionnaire contient les scalers."""
        import os
        monkeypatch.chdir(Path(__file__).parent.parent)

        from app import load_models
        load_models.clear()
        models = load_models()

        assert 'energy_scaler' in models
        assert 'co2_scaler' in models
        assert hasattr(models['energy_scaler'], 'transform')

    def test_load_models_contains_features(self, monkeypatch):
        """Vérifie que le dictionnaire contient les features."""
        import os
        monkeypatch.chdir(Path(__file__).parent.parent)

        from app import load_models
        load_models.clear()
        models = load_models()

        assert 'energy_features' in models
        assert isinstance(models['energy_features'], list)


class TestVisualizationFunctions:
    """Tests pour les fonctions de visualisation."""

    def test_create_feature_importance_plot(self, models_path):
        """Vérifie que create_feature_importance_plot retourne une figure."""
        from app import create_feature_importance_plot

        model = joblib.load(models_path / "energy_model.joblib")
        features = joblib.load(models_path / "energy_features.joblib")

        fig = create_feature_importance_plot(model, features)

        # Vérifie que c'est une figure Plotly
        assert fig is not None
        assert hasattr(fig, 'data')
        assert hasattr(fig, 'layout')

    def test_create_feature_importance_plot_has_data(self, models_path):
        """Vérifie que le plot contient des données."""
        from app import create_feature_importance_plot

        model = joblib.load(models_path / "energy_model.joblib")
        features = joblib.load(models_path / "energy_features.joblib")

        fig = create_feature_importance_plot(model, features)

        assert len(fig.data) > 0


class TestRecommendations:
    """Tests pour la fonction get_recommendations."""

    def test_low_energy_star_recommendation(self):
        """Vérifie la recommandation pour un score ENERGY STAR faible."""
        from app import get_recommendations

        recs = get_recommendations(energy_star=30, age=20, property_gfa=50000, building_type="Office (Small/Mid)")

        assert len(recs) >= 1
        assert any("ENERGY STAR faible" in rec for rec in recs)

    def test_old_building_recommendation(self):
        """Vérifie la recommandation pour un bâtiment ancien."""
        from app import get_recommendations

        recs = get_recommendations(energy_star=70, age=60, property_gfa=50000, building_type="Office (Small/Mid)")

        assert len(recs) >= 1
        assert any("ancien" in rec for rec in recs)

    def test_large_building_recommendation(self):
        """Vérifie la recommandation pour un grand bâtiment."""
        from app import get_recommendations

        recs = get_recommendations(energy_star=70, age=20, property_gfa=150000, building_type="Office (Small/Mid)")

        assert len(recs) >= 1
        assert any("Grand bâtiment" in rec for rec in recs)

    def test_hotel_recommendation(self):
        """Vérifie la recommandation pour un hôtel."""
        from app import get_recommendations

        recs = get_recommendations(energy_star=70, age=20, property_gfa=50000, building_type="Hotel")

        assert len(recs) >= 1
        assert any("Usage intensif" in rec for rec in recs)

    def test_hospital_recommendation(self):
        """Vérifie la recommandation pour un hôpital."""
        from app import get_recommendations

        recs = get_recommendations(energy_star=70, age=20, property_gfa=50000, building_type="Hospital")

        assert len(recs) >= 1
        assert any("Usage intensif" in rec for rec in recs)

    def test_good_profile_recommendation(self):
        """Vérifie la recommandation pour un bon profil."""
        from app import get_recommendations

        recs = get_recommendations(energy_star=80, age=20, property_gfa=50000, building_type="Office (Small/Mid)")

        assert len(recs) == 1
        assert "Bon profil énergétique" in recs[0]

    def test_multiple_recommendations(self):
        """Vérifie que plusieurs recommandations peuvent être générées."""
        from app import get_recommendations

        recs = get_recommendations(energy_star=30, age=60, property_gfa=150000, building_type="Hotel")

        assert len(recs) >= 4


class TestPredictWithFallback:
    """Tests pour la fonction predict_with_fallback."""

    def test_predict_with_ml_model(self, monkeypatch):
        """Vérifie la prédiction avec le modèle ML."""
        import os
        monkeypatch.chdir(Path(__file__).parent.parent)

        from app import load_models, predict_with_fallback

        load_models.clear()
        models = load_models()

        result = predict_with_fallback(
            models, property_gfa=50000, floors=5, age=30,
            energy_star=50, building_type="Office (Small/Mid)"
        )

        predicted_energy, predicted_co2, using_ml, X, X_scaled, feature_names = result

        assert using_ml is True
        assert predicted_energy > 0
        assert predicted_co2 > 0
        assert X is not None
        assert X_scaled is not None
        assert feature_names is not None

    def test_predict_with_fallback_heuristic(self):
        """Vérifie la prédiction avec le fallback heuristique."""
        from app import predict_with_fallback

        # Passer None pour les modèles pour forcer le fallback
        result = predict_with_fallback(
            None, property_gfa=50000, floors=5, age=30,
            energy_star=50, building_type="Office (Small/Mid)"
        )

        predicted_energy, predicted_co2, using_ml, X, X_scaled, feature_names = result

        assert using_ml is False
        assert predicted_energy > 0
        assert predicted_co2 > 0
        assert X is None
        assert X_scaled is None
        assert feature_names is None

    def test_fallback_larger_building_more_energy(self):
        """Vérifie que le fallback donne plus d'énergie pour un grand bâtiment."""
        from app import predict_with_fallback

        # Petit bâtiment
        result_small = predict_with_fallback(
            None, property_gfa=10000, floors=2, age=30,
            energy_star=50, building_type="Office (Small/Mid)"
        )

        # Grand bâtiment
        result_large = predict_with_fallback(
            None, property_gfa=100000, floors=10, age=30,
            energy_star=50, building_type="Office (Small/Mid)"
        )

        assert result_large[0] > result_small[0]  # Plus d'énergie

    def test_fallback_hotel_more_than_warehouse(self):
        """Vérifie que le fallback donne plus d'énergie pour un hôtel qu'un entrepôt."""
        from app import predict_with_fallback

        result_hotel = predict_with_fallback(
            None, property_gfa=50000, floors=5, age=30,
            energy_star=50, building_type="Hotel"
        )

        result_warehouse = predict_with_fallback(
            None, property_gfa=50000, floors=5, age=30,
            energy_star=50, building_type="Warehouse"
        )

        assert result_hotel[0] > result_warehouse[0]


class TestShapFunctions:
    """Tests pour les fonctions SHAP."""

    def test_get_shap_explainer(self, monkeypatch):
        """Vérifie que get_shap_explainer retourne un explainer SHAP."""
        import os
        monkeypatch.chdir(Path(__file__).parent.parent)

        from app import load_models, get_shap_explainer

        load_models.clear()
        models = load_models()

        # Clear le cache de get_shap_explainer
        get_shap_explainer.clear()
        explainer = get_shap_explainer(models['energy_model'])

        assert explainer is not None
        assert hasattr(explainer, 'shap_values')
        assert hasattr(explainer, 'expected_value')

    def test_compute_shap_values_returns_dataframe(self, models_path, sample_features):
        """Vérifie que compute_shap_values retourne un DataFrame."""
        from app import prepare_features, compute_shap_values
        import shap

        model = joblib.load(models_path / "energy_model.joblib")
        scaler = joblib.load(models_path / "energy_scaler.joblib")
        features = joblib.load(models_path / "energy_features.joblib")

        X = prepare_features(
            sample_features['property_gfa'],
            sample_features['floors'],
            sample_features['age'],
            sample_features['energy_star'],
            sample_features['building_type'],
            features
        )
        X_scaled = scaler.transform(X)

        explainer = shap.TreeExplainer(model)
        shap_df, expected_value = compute_shap_values(explainer, X_scaled, features)

        assert isinstance(shap_df, pd.DataFrame)
        assert 'Feature' in shap_df.columns
        assert 'SHAP Value' in shap_df.columns
        assert 'Abs SHAP' in shap_df.columns

    def test_compute_shap_values_expected_value(self, models_path, sample_features):
        """Vérifie que compute_shap_values retourne une expected_value."""
        from app import prepare_features, compute_shap_values
        import shap

        model = joblib.load(models_path / "energy_model.joblib")
        scaler = joblib.load(models_path / "energy_scaler.joblib")
        features = joblib.load(models_path / "energy_features.joblib")

        X = prepare_features(
            sample_features['property_gfa'],
            sample_features['floors'],
            sample_features['age'],
            sample_features['energy_star'],
            sample_features['building_type'],
            features
        )
        X_scaled = scaler.transform(X)

        explainer = shap.TreeExplainer(model)
        shap_df, expected_value = compute_shap_values(explainer, X_scaled, features)

        assert expected_value is not None
        # expected_value peut être un scalaire ou un array numpy
        if hasattr(expected_value, '__len__'):
            assert len(expected_value) > 0
            assert expected_value[0] > 0
        else:
            assert isinstance(expected_value, (int, float, np.floating))

    def test_create_shap_waterfall_plot(self, models_path, sample_features):
        """Vérifie que create_shap_waterfall_plot retourne une figure."""
        from app import prepare_features, compute_shap_values, create_shap_waterfall_plot
        import shap

        model = joblib.load(models_path / "energy_model.joblib")
        scaler = joblib.load(models_path / "energy_scaler.joblib")
        features = joblib.load(models_path / "energy_features.joblib")

        X = prepare_features(
            sample_features['property_gfa'],
            sample_features['floors'],
            sample_features['age'],
            sample_features['energy_star'],
            sample_features['building_type'],
            features
        )
        X_scaled = scaler.transform(X)
        predicted_energy = model.predict(X_scaled)[0]

        explainer = shap.TreeExplainer(model)
        shap_df, expected_value = compute_shap_values(explainer, X_scaled, features)

        fig = create_shap_waterfall_plot(shap_df, expected_value, predicted_energy)

        assert fig is not None
        assert hasattr(fig, 'data')
        assert hasattr(fig, 'layout')
