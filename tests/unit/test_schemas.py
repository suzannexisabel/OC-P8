import pytest
from pydantic import ValidationError

from app.schemas import PredictionInput

@pytest.mark.unit
def test_schema_accepts_valid_payload(valid_payload):
    payload = PredictionInput(**valid_payload)

    assert payload.app_gender == "F"
    assert payload.app_contract_type == "Cash loans"


@pytest.mark.unit
def test_schema_accepts_optional_field_null(valid_payload):
    valid_payload["bureau_nb_credits"] = None

    payload = PredictionInput(**valid_payload)

    assert payload.bureau_nb_credits is None


@pytest.mark.unit
def test_schema_rejects_invalid_gender(valid_payload):
    valid_payload["app_gender"] = "X"

    with pytest.raises(ValidationError):
        PredictionInput(**valid_payload)


@pytest.mark.unit
def test_schema_rejects_extra_field(valid_payload):
    valid_payload["unknown_column"] = 123

    with pytest.raises(ValidationError):
        PredictionInput(**valid_payload)


@pytest.mark.unit
def test_schema_rejects_out_of_range_hour(valid_payload):
    valid_payload["app_application_hour"] = 30

    with pytest.raises(ValidationError):
        PredictionInput(**valid_payload)


@pytest.mark.unit
def test_schema_rejects_empty_string_for_float(valid_payload):
    valid_payload["bureau_nb_credits"] = ""

    with pytest.raises(ValidationError):
        PredictionInput(**valid_payload)