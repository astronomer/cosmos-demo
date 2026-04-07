"Contains profile mappings used in the project"

import os

from cosmos import ProfileConfig
from cosmos.profiles import PostgresUserPasswordProfileMapping

DBT_PROFILE = os.getenv("DBT_PROFILE", "postgres")

if DBT_PROFILE == "bigquery":
    from cosmos.profiles import GoogleCloudServiceAccountDictProfileMapping

    default_profile = ProfileConfig(
        profile_name="default",
        target_name="dev",
        profile_mapping=GoogleCloudServiceAccountDictProfileMapping(
            conn_id="gcp_gs_conn",
            profile_args={"dataset": os.environ["GCP_BQ_DATASET"], "project": os.environ["GCP_PROJECT_ID"]},
        ),
    )
else:
    default_profile = ProfileConfig(
        profile_name="airflow_db",
        target_name="dev",
        profile_mapping=PostgresUserPasswordProfileMapping(
            conn_id="airflow_metadata_db",
            profile_args={"schema": "dbt"},
        ),
    )

# Keep backward compatibility
airflow_db = default_profile
