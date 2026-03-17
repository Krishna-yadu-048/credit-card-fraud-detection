from dagster import Definitions

from orchestration.assets import (
    drift_report,
    evaluated_model,
    raw_data,
    trained_model,
    validated_data,
)
from orchestration.schedules import daily_drift_check, weekly_retraining

defs = Definitions(
    assets=[raw_data, validated_data, trained_model, evaluated_model, drift_report],
    schedules=[weekly_retraining, daily_drift_check],
)
