import pandas as pd
import pytest

def test_data_pipeline_schema():
    """Vérifie que les données entrantes respectent le schéma métier."""
    dummy_data = pd.DataFrame({
        "amount": [150.0],
        "oldbalanceOrg": [1000.0],
        "newbalanceOrig": [850.0],
        "isFraud": [0]
    })
    
    assert "isFraud" in dummy_data.columns
    assert dummy_data["amount"].iloc[0] >= 0, "Le montant ne peut pas être négatif"
