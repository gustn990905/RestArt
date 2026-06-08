import os
from typing import Dict


def get_db_config() -> Dict[str, object]:
    """
    Return database connection settings from environment variables.

    This project keeps actual database credentials outside the repository.
    Use `.env.example` as a reference for required variable names.
    """

    return {
        "host": os.getenv("DB_HOST", "localhost"),
        "port": int(os.getenv("DB_PORT", "3306")),
        "user": os.getenv("DB_USER", "root"),
        "password": os.getenv("DB_PASSWORD", ""),
        "database": os.getenv("DB_NAME", "restartdb"),
        "charset": os.getenv("DB_CHARSET", "utf8mb4"),
    }


def get_database_url() -> str:
    """
    Build SQLAlchemy-compatible MySQL database URL from environment variables.
    """

    db_config = get_db_config()

    return (
        f"mysql+pymysql://{db_config['user']}:{db_config['password']}"
        f"@{db_config['host']}:{db_config['port']}/{db_config['database']}"
    )