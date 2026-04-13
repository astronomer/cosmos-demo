import os
from datetime import datetime

from cosmos import DbtDag, ProjectConfig, ExecutionConfig, RenderConfig, ExecutionMode, TestBehavior
from include.constants import jaffle_shop_path, dbt_executable
from include.profiles import default_profile


DBT_ADAPTER_VERSION = os.getenv("DBT_ADAPTER_VERSION", "1.9")

simple_dag_async = DbtDag(
    # dbt/cosmos-specific parameters
    project_config=ProjectConfig(
        jaffle_shop_path,
    ),
    profile_config=default_profile,
    execution_config=ExecutionConfig(
        execution_mode=ExecutionMode.AIRFLOW_ASYNC,
        async_py_requirements=[f"dbt-bigquery=={DBT_ADAPTER_VERSION}"],
        dbt_executable_path=str(dbt_executable),
    ),
    render_config=RenderConfig(test_behavior=TestBehavior.NONE),
    # normal dag parameters
    schedule=None,
    start_date=datetime(2023, 1, 1),
    catchup=False,
    dag_id="simple_dag_async",
    tags=["simple"],
    operator_args={
        "location": "US",
        "install_deps": True,
        "full_refresh": True,
    },
)
# [END airflow_async_execution_mode_example]