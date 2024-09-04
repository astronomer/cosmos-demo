FROM quay.io/astronomer/astro-runtime:11.10.0-python-3.11

# install dbt into a virtual environment
#RUN python -m venv dbt_venv && source dbt_venv/bin/activate && \
#    pip install --no-cache-dir --upgrade dbt-postgres>=1.7 && deactivate
#
RUN python -m venv dbt_venv && source dbt_venv/bin/activate && \
    pip install --no-cache-dir dbt-postgres==1.5.4 dbt-bigquery && deactivate

#COPY astronomer_cosmos-1.5.1-py3-none-any.whl astronomer_cosmos-1.5.2-py3-none-any.whl
#RUN pip install --no-cache-dir astronomer_cosmos-1.5.2-py3-none-any.whl

#COPY astronomer_cosmos-1.6.0a6-py3-none-any.whl astronomer_cosmos-1.6.0a6-py3-none-any.whl
#RUN pip install --no-cache-dir astronomer_cosmos-1.6.0a6-py3-none-any.whl

# set a connection to the airflow metadata db to use for testing
ENV AIRFLOW_CONN_AIRFLOW_METADATA_DB=postgresql+psycopg2://postgres:postgres@postgres:5432/postgres

# Enable test connection for increasing local development productivity
ENV AIRFLOW__CORE__TEST_CONNECTION=Enabled

ENV OPENLINEAGE_DISABLED=True
ENV AIRFLOW__COSMOS__ENABLE_CACHE=1
ENV AIRFLOW__COSMOS__EXPERIMENTAL_CACHE=1
ENV AIRFLOW__COSMOS__REMOTE_CACHE_DIR="s3://cosmos-remote-cache/cosmos/"
ENV AIRFLOW__COSMOS__REMOTE_CACHE_DIR_CONN_ID="aws_s3_conn"

#ENV AIRFLOW__COSMOS__REMOTE_CACHE_DIR="gs://cosmos-manifest-test/cosmos/"
#ENV AIRFLOW__COSMOS__REMOTE_CACHE_DIR_CONN_ID="gcp_gs_conn"

ENV POSTGRES_DB=postgres
ENV POSTGRES_SCHEMA=dbt

COPY key.json /usr/local/airflow/dbt/jaffle_shop/key.json