import logging
import logging.config
import os
from google.cloud import logging as gcp_logging

LOGGING: dict = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "json": {
            "class": "pythonjsonlogger.jsonlogger.JsonFormatter",
            "format": "%(asctime)s %(name)s %(levelname)s %(module)s %(message)s %(pathname)s %(lineno)s %(funcName)s %(threadName)s %(thread)s %(process)s %(processName)s",  # noqa: E501
            "datefmt": "%Y-%m-%d %H:%M:%S",
        },
        "stdout": {
            "format": "%(levelname)s: %(asctime)s - %(name)s - %(module)s - %(message)s",
            "datefmt": "%Y-%m-%d %H:%M:%S",
        },
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "stdout",
            "level": "DEBUG",
        },
        "json_file": {
            "class": "logging.handlers.TimedRotatingFileHandler",
            "level": "DEBUG",
            "formatter": "json",
            "filename": "logs/logs.json",
            "when": "midnight",
            "interval": 1,
            "backupCount": 30,
        },
    },
    "loggers": {
        "devel": {
            "handlers": [
                "console",
                "json_file",
            ],
            "level": "DEBUG",
            "propagate": "True",
        },
        "prod": {
            "handlers": [
                "console",
                "json_file",
            ],
            "level": "DEBUG",
        },
    },
}


def create_cloud_handler(test: bool = False) -> dict:
    labels = {"env": "prod", "app": "orcestra-api"}
    if test:
        labels["env"] = labels["env"] + "-test"
    return {
        "cloud_logging": {
            "class": "google.cloud.logging.handlers.CloudLoggingHandler",
            "client": gcp_logging.Client(),
            "level": "DEBUG",
            "formatter": "json",
            "labels" : labels
        }
    }


def setup_logger(logger_name: str, test: bool = False) -> logging.Logger:
    valid_loggers = ["devel", "prod"]
    assert (
        logger_name in valid_loggers
    ), f"Invalid logger name. Available options are {valid_loggers}"

    if logger_name == "prod":
        cloud_handler = create_cloud_handler(test)
        LOGGING["handlers"].update(cloud_handler)
        LOGGING["loggers"]["prod"]["handlers"].append("cloud_logging")

    logging.config.dictConfig(LOGGING)

    return logging.getLogger(logger_name)


def get_logger() -> logging.Logger:
    env = os.environ.get("ENV")
    if not env:
        raise ValueError("ENV not set for logger")
    return setup_logger(env)