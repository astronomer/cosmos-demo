from datetime import datetime

from cosmos.airflow.dag import DbtDag
from cosmos.config import ExecutionConfig, ProfileConfig, ProjectConfig, RenderConfig, InvocationMode
from cosmos.constants import ExecutionMode
from include.profiles import default_profile
from include.constants import jaffle_shop_path, dbt_executable


# [START example_watcher]
example_watcher = DbtDag(
    # dbt/cosmos-specific parameters
    execution_config=ExecutionConfig(
        execution_mode=ExecutionMode.WATCHER,
        dbt_executable_path=str(dbt_executable),
    ),
    project_config=ProjectConfig(jaffle_shop_path),
    render_config=RenderConfig(invocation_mode=InvocationMode.SUBPROCESS, dbt_executable_path=str(dbt_executable)),
    profile_config=default_profile,
    # normal dag parameters
    schedule="@daily",
    start_date=datetime(2023, 1, 1),
    catchup=False,
    dag_id="example_watcher",
    default_args={"retries": 0},
)
# [END example_watcher]