import logging
from .utils.logging_config import CustomFormatter
import os
from logtail import LogtailHandler


def configure_logger():
    logger = logging.getLogger()  # root logger
    log_level = logging.getLevelName(os.environ.get("LOG_LEVEL", "DEBUG"))
    logger.setLevel(log_level)

    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(os.environ.get("LOG_LEVEL", logging.DEBUG))
    stream_handler.setFormatter(CustomFormatter())

    logger.addHandler(stream_handler)

    if os.environ.get("BETTERSTACK_API_TOKEN"):
        betterstack_handler = LogtailHandler(
            source_token=os.environ.get("BETTERSTACK_API_TOKEN")
        )
        logger.addHandler(betterstack_handler)

    logging.getLogger("watchfiles.main").setLevel(logging.WARNING)


configure_logger()
