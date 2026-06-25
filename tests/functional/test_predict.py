import pytest


@pytest.mark.functional
# Test complet avec donnees valide
def test_predict_success(client, valid_payload):
    response = client.post("/predict", json=valid_payload)

    assert response.status_code == 200
    assert response.json() == {
        "prediction": 1,
        "probability": 0.8,
        "threshold": 0.54
    }

@pytest.mark.functional
# Test avec une entrée non obligatoire vide 
def test_predict_optional_field_null(client, valid_payload):
    valid_payload["bureau_nb_credits"] = None

    response = client.post("/predict", json=valid_payload)

    assert response.status_code == 200


@pytest.mark.functional
# Test avec une entree non obligatoire manquante
def test_predict_optional_field_missing(client, valid_payload):
    valid_payload.pop("bureau_nb_credits")

    response = client.post("/predict", json=valid_payload)

    assert response.status_code == 200

@pytest.mark.functional
# Test avec entree obligatoire manquante
def test_predict_missing_required_field(client, valid_payload):
    valid_payload.pop("app_gender")

    response = client.post("/predict", json=valid_payload)

    assert response.status_code == 422


@pytest.mark.functional
#test avec donnee cat non valide 
def test_predict_invalid_category(client, valid_payload):
    valid_payload["app_gender"] = "X"

    response = client.post("/predict", json=valid_payload)

    assert response.status_code == 422

@pytest.mark.functional
# Test avec donnee exterieur fourchette
def test_predict_extra_field_forbidden(client, valid_payload):
    valid_payload["unknown_column"] = 123

    response = client.post("/predict", json=valid_payload)

    assert response.status_code == 422

