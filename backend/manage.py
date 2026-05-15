#!/usr/bin/env python
"""
QueueSenseAI - Django administrative utility.

Supports:
- Environment variable loading (.env)
- Multiple settings environments
- Better error handling
- Production-ready startup
"""

import os
import sys
from pathlib import Path


# =========================================================
# BASE DIRECTORY
# =========================================================
BASE_DIR = Path(__file__).resolve().parent


# =========================================================
# LOAD ENVIRONMENT VARIABLES
# =========================================================
def load_env():
    """
    Load environment variables from .env file.
    """

    env_path = BASE_DIR / ".env"

    if env_path.exists():
        try:
            from dotenv import load_dotenv

            load_dotenv(dotenv_path=env_path)

            print("✓ Environment variables loaded")

        except ImportError:
            print(
                "\n[WARNING] python-dotenv is not installed."
                "\nInstall using:"
                "\npip install python-dotenv\n"
            )
    else:
        print("[INFO] .env file not found")


# =========================================================
# MAIN FUNCTION
# =========================================================
def main():
    """
    Run Django administrative tasks.
    """

    # Load .env variables
    load_env()

    # Default Django settings module
    os.environ.setdefault(
        "DJANGO_SETTINGS_MODULE",
        "config.settings.development"
    )

    try:
        from django.core.management import execute_from_command_line

    except ImportError as exc:
        raise ImportError(
            "\n❌ Couldn't import Django."
            "\n\nPossible reasons:"
            "\n1. Virtual environment is not activated"
            "\n2. Django is not installed"
            "\n3. Requirements are missing"
            "\n4. PYTHONPATH issue"
            "\n\nInstall dependencies:"
            "\npip install -r requirements.txt\n"
        ) from exc

    # Execute Django command
    execute_from_command_line(sys.argv)


# =========================================================
# ENTRY POINT
# =========================================================
if __name__ == "__main__":
    main()