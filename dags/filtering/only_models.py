from datetime import datetime

from cosmos import DbtDag, ProjectConfig, RenderConfig

from include.profiles import airflow_db
from include.constants import jaffle_shop_path, venv_execution_config

only_models = DbtDag(
    project_config=ProjectConfig(jaffle_shop_path),
    profile_config=airflow_db,
    execution_config=venv_execution_config,
    # new render config
    render_config=RenderConfig(
        select=["path:models"],
    ),
    # normal dag parameters
    schedule_interval="@daily",
    start_date=datetime(2023, 1, 1),
    catchup=False,
    dag_id="only_models",
    tags=["filtering"],
)
