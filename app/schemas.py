from pydantic import BaseModel, Field, ConfigDict
from typing import Literal
from typing import Optional

class PredictionInput(BaseModel):
    app_contract_type: str
    app_gender: str
    app_owns_car: str
    app_owns_realty: str
    app_client_income: float
    app_accompanied_by: Optional[str] = None
    app_income_type: str
    app_education_level: str
    app_family_status: str
    app_housing_type: str
    app_region_density: float
    app_client_age_days: int
    app_id_last_update_days: int
    app_car_age: Optional[float] = None
    app_occupation_type: Optional[str] = None
    app_household_size: float
    app_region_risk_rating: int
    app_application_weekday: str
    app_application_hour: int
    app_employer_type: str
    app_phone_last_change_days: Optional[float] = None
    app_is_unemployed: int
    app_contact_score: int
    app_documents_provided: int
    app_housing_quality_avg: Optional[float] = None
    app_housing_quality_variability: Optional[float] = None
    app_housing_info_missing_ratio: float
    app_external_risk_score: Optional[float] = None
    app_social_risk_score: Optional[float] = None
    app_credit_vs_goods_value: Optional[float] = None
    app_credit_vs_income: float
    app_region_mismatch_count: int
    app_city_mismatch_count: int
    app_total_credit_requests: float
    app_employment_ratio: Optional[float] = None
    app_registration_ratio: float
    bureau_nb_credits: Optional[float] = None
    bureau_nb_currency_types: Optional[float] = None
    bureau_main_credit_currency: Optional[str] = None
    bureau_avg_days_since_credit: Optional[float] = None
    bureau_avg_credit_prolongation: Optional[float] = None
    bureau_avg_credit_amount: Optional[float] = None
    bureau_avg_outstanding_debt: Optional[float] = None
    bureau_avg_credit_limit: Optional[float] = None
    bureau_nb_credit_types: Optional[float] = None
    bureau_main_credit_type: Optional[str] = None
    bureau_nb_credits_with_overdue: Optional[float] = None
    bureau_avg_closing_delay: Optional[float] = None
    bureau_has_active_credit: Optional[float] = None
    bureau_avg_credit_duration_months: Optional[float] = None
    bureau_pct_business_credit: Optional[float] = None
    bureau_pct_other_credit: Optional[float] = None
    bureau_pct_rare_credit: Optional[float] = None
    prev_loan_count: Optional[float] = None
    prev_annuity_avg: Optional[float] = None
    prev_installments_avg: Optional[float] = None
    prev_revolving_ratio: Optional[float] = None
    prev_loyalty_ratio: Optional[float] = None
    prev_channel_country_ratio: Optional[float] = None
    prev_channel_store_ratio: Optional[float] = None
    prev_high_yield_ratio: Optional[float] = None
    prev_low_yield_ratio: Optional[float] = None
    prev_credit_to_annuity_ratio: Optional[float] = None
    prev_credit_per_loan: Optional[float] = None