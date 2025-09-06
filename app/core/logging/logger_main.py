"""
Module for logging software actions

Модуль для логгирования действий софта
"""

from loguru import logger
from pathlib import Path


logs_dir = Path("logs")
logs_dir.mkdir(exist_ok=True)

# Remove default log handlers
logger.remove()

# Console logging with color
logger.add(
    sink=lambda msg: print(msg, end=""),
    colorize=True,
    format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | "
           "<level>{level: <8}</level> | "
           "<cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - "
           "<level>{message}</level>"  
)

# File logging with rotation and retention
logger.add(
    logs_dir / "software_logs.log",
    rotation="5 MB",
    retention="10 days",
    enqueue=True,
    format="{time:YYYY-MM-DD HH:mm:ss} | {level: <8} | {name}:{function}:{line} - {message}"
)