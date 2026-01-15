import os
import pathlib
from functools import lru_cache


class BaseConfig:
    BASE_DIR: pathlib.Path = pathlib.Path(__file__).parent.parent

    DATABASE_URL: str = os.environ.get(
        "DATABASE_URL", f"sqlite:///{BASE_DIR}/db.sqlite3"
    )
    DATABASE_CONNECT_DICT: dict = {}

    CELERY_BROKER_URL: str = os.environ.get(
        "CELERY_BROKER_URL", "redis://127.0.0.1:6379/0"
    )
    RESULT_BACKEND: str = (
        os.environ.get(  # Based on deprecation warning from CELERY_RESULT_BACKEND
            "CELERY_RESULT_BACKEND", "redis://127.0.0.1:6379/0"
        )
    )


class DevelopmentConfig(BaseConfig):
    CELERY_TASK_ALWAYS_EAGER: bool = True
    pass


class ProductionConfig(BaseConfig):
    pass


class TestingConfig(BaseConfig):
    pass


@lru_cache()  # Least Recently Used Cache - This makes it so the program only loads the config once and then uses the cached version for the rest of the program.
def get_settings():
    config_cls_dict = {
        "development": DevelopmentConfig,
        "production": ProductionConfig,
        "testing": TestingConfig,
    }

    config_name = os.environ.get("FASTAPI_CONFIG", "development")
    config_cls = config_cls_dict[config_name]
    return config_cls()


settings = get_settings()
