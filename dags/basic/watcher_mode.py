from datetime import datetime

from cosmos.airflow.dag import DbtDag
from cosmos.config import ExecutionConfig, ProfileConfig, ProjectConfig, RenderConfig, InvocationMode
from cosmos.constants import ExecutionMode
from include.profiles import bigquery_db
from include.constants import jaffle_shop_path, watcher_execution_config, dbt_executable

operator_args = {
    "install_deps": True,  # install any necessary dependencies before running any dbt command
}

# [START example_watcher]
example_watcher = DbtDag(
    # dbt/cosmos-specific parameters
    execution_config=watcher_execution_config,
    project_config=ProjectConfig(jaffle_shop_path),
    render_config=RenderConfig(invocation_mode=InvocationMode.SUBPROCESS, dbt_executable_path=str(dbt_executable)),
    profile_config=bigquery_db,
    operator_args=operator_args,
    # normal dag parameters
    schedule="@daily",
    start_date=datetime(2023, 1, 1),
    catchup=False,
    dag_id="example_watcher",
    default_args={"retries": 0},
)
# [END example_watcher]