from dagster import repository, with_resources
from dagster_dbt import dbt_cli_resource
from dagster_dbt import load_assets_from_dbt_project

DBT_PROJECT_PATH = "app/dbt_parent"
DBT_PROFILES = "app/dbt_parent"

assets = load_assets_from_dbt_project(
    project_dir=DBT_PROJECT_PATH, profiles_dir=DBT_PROFILES, key_prefix=["dbt_parent"]
)


@repository
def {{project_name | replace("-", "_")}}():
    return with_resources(
        assets,
        {
            "dbt": dbt_cli_resource.configured(
                {
                    "project_dir": DBT_PROJECT_PATH,
                    "profiles_dir": DBT_PROFILES,
                },
            ),
        },
    )
