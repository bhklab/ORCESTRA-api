import logging
import logging.config
from google.cloud import logging as gcp_logging
from pythonjsonlogger import jsonlogger

LOGGING: dict = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "json": {
            "class": "pythonjsonlogger.jsonlogger.JsonFormatter",
            "format": "%(asctime)s %(name)s %(levelname)s %(module)s %(message)s %(pathname)s %(lineno)s %(funcName)s %(threadName)s %(thread)s %(process)s %(processName)s",
            "datefmt": "%Y-%m-%d %H:%M:%S",
        },
        "stdout": {
            "format": "%(asctime)s - %(name)s - %(levelname)s - %(module)s - %(message)s",
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
        "development": {
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


def setup_logger(logger_name: str) -> logging.Logger:
    assert logger_name in [
        "development",
        "prod",
    ], "Invalid logger name. Available options are 'development' or 'prod'"

    if logger_name == "prod":
        cloud_handler = {
            "cloud_logging": {
                "class": "google.cloud.logging.handlers.CloudLoggingHandler",
                "client": gcp_logging.Client(),
                "level": "DEBUG",
                "formatter": "json",
            }
        }
        LOGGING["handlers"].update(cloud_handler)
        LOGGING["loggers"]["prod"]["handlers"].append("cloud_logging")

    logging.config.dictConfig(LOGGING)

    return logging.getLogger(logger_name)


if __name__ == "__main__":

    logger = setup_logger("development")

    logger.info("This is an info log")
