import sys
import pytest
from fastapi.testclient import TestClient

#Definition du dummy pipline pour test

class DummyPipeline:
    classes_ = [0, 1]

    def predict_proba(self, X):
        import numpy as np
        return np.tile([0.2, 0.8], (len(X), 1))



@pytest.fixture
def client(monkeypatch):
    import mlflow.sklearn

    monkeypatch.setattr(
        mlflow.sklearn,
        "load_model",
        lambda path: DummyPipeline()
    )

    sys.modules.pop("app.model", None)
    sys.modules.pop("app.main", None)

    from app.main import app

    return TestClient(app)


@pytest.fixture
def valid_payload():
    return {
        "app_contract_type": "Cash loans",
        "app_gender": "F",
        "app_owns_car": "N",
        "app_owns_realty": "Y",
        "app_client_income": 12.5,
        "app_accompanied_by": "Unaccompanied",
        "app_income_type": "Working",
        "app_education_level": "Higher education",
        "app_family_status": "Married",
        "app_housing_type": "House / apartment",
        "app_region_density": 0.01,
        "app_client_age_days": -12000,
        "app_id_last_update_days": -1000,
        "app_car_age": 5.0,
        "app_occupation_type": "Laborers",
        "app_household_size": 2.0,
        "app_region_risk_rating": 2,
        "app_application_weekday": "MONDAY",
        "app_application_hour": 10,
        "app_employer_type": "Business Entity Type 3",
        "app_phone_last_change_days": -500.0,
        "app_is_unemployed": 0,
        "app_contact_score": 8,
        "app_documents_provided": 2,
        "app_housing_quality_avg": 0.5,
        "app_housing_quality_variability": 0.1,
        "app_housing_info_missing_ratio": 0.2,
        "app_external_risk_score": 0.4,
        "app_social_risk_score": 10.0,
        "app_credit_vs_goods_value": 1.2,
        "app_credit_vs_income": 50000.0,
        "app_region_mismatch_count": 0,
        "app_city_mismatch_count": 0,
        "app_total_credit_requests": 1.0,
        "app_employment_ratio": 0.3,
        "app_registration_ratio": 0.5,
        "bureau_nb_credits": 3.0,
        "bureau_nb_currency_types": 1.0,
        "bureau_main_credit_currency": "currency 1",
        "bureau_avg_days_since_credit": -500.0,
        "bureau_avg_credit_prolongation": 0.0,
        "bureau_avg_credit_amount": 100000.0,
        "bureau_avg_outstanding_debt": 20000.0,
        "bureau_avg_credit_limit": 50000.0,
        "bureau_nb_credit_types": 2.0,
        "bureau_main_credit_type": "CONSUMER",
        "bureau_nb_credits_with_overdue": 0.0,
        "bureau_avg_closing_delay": -100.0,
        "bureau_has_active_credit": 1.0,
        "bureau_avg_credit_duration_months": 24.0,
        "bureau_pct_business_credit": 0.0,
        "bureau_pct_other_credit": 0.0,
        "bureau_pct_rare_credit": 0.0,
        "prev_loan_count": 2.0,
        "prev_annuity_avg": 12000.0,
        "prev_installments_avg": 12.0,
        "prev_revolving_ratio": 0.1,
        "prev_loyalty_ratio": 0.3,
        "prev_channel_country_ratio": 0.5,
        "prev_channel_store_ratio": 0.2,
        "prev_high_yield_ratio": 0.1,
        "prev_low_yield_ratio": 0.4,
        "prev_credit_to_annuity_ratio": 10.0,
        "prev_credit_per_loan": 100000.0
    }