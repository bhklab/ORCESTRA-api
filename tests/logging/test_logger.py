import logging
import os
import pytest
from unittest.mock import MagicMock
from logging import config as logging_config
from logging.handlers import TimedRotatingFileHandler
from google.cloud import logging as gcp_logging

from orcestrator.common import setup_logger, LOGGING


@pytest.fixture(scope="function")
def cleanup_log_file():
    log_file = "logs/logs.json"
    if os.path.exists(log_file):
        os.remove(log_file)
    yield
    if os.path.exists(log_file):
        os.remove(log_file)


def test_logger_configuration_devel():
    logger = setup_logger("devel", test=True)

    assert logger.name == "devel"
    assert len(logger.handlers) == 2
    assert any(isinstance(h, logging.StreamHandler) for h in logger.handlers)
    assert any(isinstance(h, TimedRotatingFileHandler) for h in logger.handlers)

    console_handler = next(
        h for h in logger.handlers if isinstance(h, logging.StreamHandler)
    )
    file_handler = next(
        h for h in logger.handlers if isinstance(h, TimedRotatingFileHandler)
    )

    assert console_handler.formatter._fmt == LOGGING["formatters"]["stdout"]["format"]  # type: ignore
    assert file_handler.formatter._fmt == LOGGING["formatters"]["json"]["format"]  # type: ignore


def test_logger_configuration_prod():
    logger = setup_logger("prod", test=True)

    assert logger.name == "prod"
    assert len(logger.handlers) == 3
    assert any(isinstance(h, logging.StreamHandler) for h in logger.handlers)
    assert any(isinstance(h, TimedRotatingFileHandler) for h in logger.handlers)

    cloud_handler = next(
        h
        for h in logger.handlers
        if isinstance(h, gcp_logging.handlers.CloudLoggingHandler)
    )

    assert cloud_handler.name == "cloud_logging"
    assert cloud_handler.level == logging.DEBUG
    assert cloud_handler.labels == {"env": "prod-test", "app": "orcestra-api"}
    assert cloud_handler.formatter._fmt == LOGGING["formatters"]["json"]["format"]  # type: ignore

    logger.info("Test prod log info")
    logger.debug("Test prod log debug")


def test_logging_to_console(capsys):
    logger = setup_logger("devel", test=True)
    logger.debug("Test console log")

    captured = capsys.readouterr()

    assert "Test console log" in captured.err


def test_logging_to_file(cleanup_log_file):
    logger = setup_logger("devel", test=True)
    logger.debug("Test file log")

    with open("logs/logs.json", "r") as f:
        log_content = f.read()

    assert "Test file log" in log_content


def test_logging_to_gcp(mocker):
    mock_cloud_handler = mocker.patch(
        "google.cloud.logging.handlers.CloudLoggingHandler.emit", autospec=True
    )

    logger = setup_logger("prod", test=True)
    logger.debug("Test GCP log")

    mock_cloud_handler.assert_called()
