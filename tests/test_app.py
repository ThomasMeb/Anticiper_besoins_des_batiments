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
