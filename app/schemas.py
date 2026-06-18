from pydantic import BaseModel, Field, ConfigDict
from typing import Literal, Optional
from typing_extensions import Annotated


# =========================
# Types numériques
# =========================

Ratio = Annotated[float, Field(ge=0, le=1)]
BinaryInt = Annotated[int, Field(ge=0, le=1)]

ApplicationHour = Annotated[int, Field(ge=0, le=23)]
RegionRiskRating = Annotated[int, Field(ge=1, le=3)]


# =========================
# Catégories principales
# =========================

ContractType = Literal["Cash loans", "Revolving loans"]
Gender = Literal["M", "F"]
YesNo = Literal["N", "Y"]

Weekday = Literal[
    "MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY",
    "FRIDAY", "SATURDAY", "SUNDAY"
]

AccompaniedBy = Literal[
    "Unaccompanied", "Family", "Spouse, partner", "Children",
    "Other_A", "Other_B", "Group of people"
]

IncomeType = Literal[
    "Working", "State servant", "Commercial associate", "Pensioner",
    "Unemployed", "Student", "Businessman", "Maternity leave"
]

EducationLevel = Literal[
    "Secondary / secondary special", "Higher education",
    "Incomplete higher", "Lower secondary", "Academic degree"
]

FamilyStatus = Literal[
    "Single / not married", "Married", "Civil marriage",
    "Widow", "Separated"
]

HousingType = Literal[
    "House / apartment", "Rented apartment", "With parents",
    "Municipal apartment", "Office apartment", "Co-op apartment"
]

OccupationType = Literal[
    "Laborers", "Core staff", "Accountants", "Managers", "Drivers",
    "Sales staff", "Cleaning staff", "Cooking staff",
    "Private service staff", "Medicine staff", "Security staff",
    "High skill tech staff", "Waiters/barmen staff",
    "Low-skill Laborers", "Realty agents", "Secretaries",
    "IT staff", "HR staff"
]

EmployerType = Literal[
    "Business Entity Type 3", "School", "Government", "Religion",
    "Other", "XNA", "Electricity", "Medicine",
    "Business Entity Type 2", "Self-employed", "Transport: type 2",
    "Construction", "Housing", "Kindergarten", "Trade: type 7",
    "Industry: type 11", "Military", "Services",
    "Security Ministries", "Transport: type 4", "Industry: type 1",
    "Emergency", "Security", "Trade: type 2", "University",
    "Transport: type 3", "Police", "Business Entity Type 1",
    "Postal", "Industry: type 4", "Agriculture", "Restaurant",
    "Culture", "Hotel", "Industry: type 7", "Trade: type 3",
    "Industry: type 3", "Bank", "Industry: type 9", "Insurance",
    "Trade: type 6", "Industry: type 2", "Transport: type 1",
    "Industry: type 12", "Mobile", "Trade: type 1",
    "Industry: type 5", "Industry: type 10", "Legal Services",
    "Advertising", "Trade: type 5", "Cleaning",
    "Industry: type 13", "Trade: type 4", "Telecom",
    "Industry: type 8", "Realtor", "Industry: type 6"
]

BureauCurrency = Literal["currency 1", "currency 2", "currency 3"]

BureauCreditType = Literal[
    "CONSUMER", "ASSET", "OTHER", "BUSINESS", "RARE"
]


# =========================
# Schéma API
# =========================

class PredictionInput(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
        strict=True
    )

    # ---------- Application principale ----------
    app_contract_type: ContractType
    app_gender: Gender
    app_owns_car: YesNo
    app_owns_realty: YesNo

    app_client_income: Annotated[float, Field(ge=10.15, le=18.58)]
    app_accompanied_by: Optional[AccompaniedBy] = None
    app_income_type: IncomeType
    app_education_level: EducationLevel
    app_family_status: FamilyStatus
    app_housing_type: HousingType

    app_region_density: Annotated[float, Field(ge=0.00029, le=0.072508)]
    app_client_age_days: Annotated[int, Field(ge=-25229, le=-7489)]
    app_id_last_update_days: Annotated[int, Field(ge=-7197, le=0)]
    app_car_age: Optional[Annotated[float, Field(ge=0, le=91)]] = None
    app_occupation_type: Optional[OccupationType] = None

    app_household_size: Annotated[float, Field(ge=1, le=20)]
    app_region_risk_rating: RegionRiskRating
    app_application_weekday: Weekday
    app_application_hour: ApplicationHour
    app_employer_type: EmployerType
    app_phone_last_change_days: Optional[Annotated[float, Field(ge=-4292, le=0)]] = None

    # ---------- Indicateurs application ----------
    app_is_unemployed: BinaryInt
    app_contact_score: Annotated[int, Field(ge=3, le=13)]
    app_documents_provided: Annotated[int, Field(ge=0, le=4)]

    app_housing_quality_avg: Optional[Annotated[float, Field(ge=0, le=0.9836)]] = None
    app_housing_quality_variability: Optional[Annotated[float, Field(ge=0, le=0.532371)]] = None
    app_housing_info_missing_ratio: Ratio

    app_external_risk_score: Optional[Annotated[float, Field(ge=0, le=0.878904)]] = None
    app_social_risk_score: Optional[Annotated[float, Field(ge=0, le=404)]] = None

    app_credit_vs_goods_value: Optional[Annotated[float, Field(ge=0.15, le=6)]] = None
    app_credit_vs_income: Annotated[float, Field(ge=3409.26, le=313670.3)]

    app_region_mismatch_count: Annotated[int, Field(ge=0, le=3)]
    app_city_mismatch_count: Annotated[int, Field(ge=0, le=3)]
    app_total_credit_requests: Annotated[float, Field(ge=0, le=262)]

    app_employment_ratio: Optional[Annotated[float, Field(ge=0, le=0.728812)]] = None
    app_registration_ratio: Annotated[float, Field(ge=0, le=1.000004)]

    # ---------- Bureau crédit ----------
    bureau_nb_credits: Optional[Annotated[float, Field(ge=1, le=116)]] = None
    bureau_nb_currency_types: Optional[Annotated[float, Field(ge=1, le=3)]] = None
    bureau_main_credit_currency: Optional[BureauCurrency] = None

    bureau_avg_days_since_credit: Optional[Annotated[float, Field(ge=-2922, le=0)]] = None
    bureau_avg_credit_prolongation: Optional[Annotated[float, Field(ge=0, le=6)]] = None
    bureau_avg_credit_amount: Optional[Annotated[float, Field(ge=0, le=198072300)]] = None
    bureau_avg_outstanding_debt: Optional[Annotated[float, Field(ge=-1083615, le=43650000)]] = None
    bureau_avg_credit_limit: Optional[Annotated[float, Field(ge=-97891.66, le=4500000)]] = None
    bureau_nb_credit_types: Optional[Annotated[float, Field(ge=1, le=4)]] = None
    bureau_main_credit_type: Optional[BureauCreditType] = None

    bureau_nb_credits_with_overdue: Optional[Annotated[float, Field(ge=0, le=7)]] = None
    bureau_avg_closing_delay: Optional[Annotated[float, Field(ge=-33357, le=2573)]] = None
    bureau_has_active_credit: Optional[Annotated[float, Field(ge=0, le=46)]] = None
    bureau_avg_credit_duration_months: Optional[Annotated[float, Field(ge=0, le=95)]] = None

    bureau_pct_business_credit: Optional[Ratio] = None
    bureau_pct_other_credit: Optional[Ratio] = None
    bureau_pct_rare_credit: Optional[Ratio] = None

    # ---------- Historique prêts précédents ----------
    prev_loan_count: Optional[Annotated[float, Field(ge=1, le=73)]] = None
    prev_annuity_avg: Optional[Annotated[float, Field(ge=0, le=300425.4)]] = None
    prev_installments_avg: Optional[Annotated[float, Field(ge=0, le=72)]] = None

    prev_revolving_ratio: Optional[Ratio] = None
    prev_loyalty_ratio: Optional[Ratio] = None
    prev_channel_country_ratio: Optional[Ratio] = None
    prev_channel_store_ratio: Optional[Ratio] = None
    prev_high_yield_ratio: Optional[Ratio] = None
    prev_low_yield_ratio: Optional[Ratio] = None

    prev_credit_to_annuity_ratio: Optional[Annotated[float, Field(ge=0, le=71.84)]] = None
    prev_credit_per_loan: Optional[Annotated[float, Field(ge=0, le=2025000)]] = None