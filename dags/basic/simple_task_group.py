from datetime import datetime

from airflow.decorators import dag
from airflow.operators.empty import EmptyOperator


from cosmos import DbtTaskGroup, ProjectConfig

from include.profiles import airflow_db
from include.constants import jaffle_shop_path, venv_execution_config


@dag(
    schedule_interval="@daily",
    start_date=datetime(2023, 1, 1),
    catchup=False,
    tags=["simple"],
)
def simple_task_group() -> None:
    """
    The simplest example of using Cosmos to render a dbt project as a TaskGroup.
    """
    pre_dbt = EmptyOperator(task_id="pre_dbt")

    jaffle_shop = DbtTaskGroup(
        group_id="my_jaffle_shop_project",
        project_config=ProjectConfig(jaffle_shop_path),
        profile_config=airflow_db,
        execution_config=venv_execution_config,
    )

    post_dbt = EmptyOperator(task_id="post_dbt")

    pre_dbt >> jaffle_shop >> post_dbt


simple_task_group()
