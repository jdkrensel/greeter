"""Main application entry point."""

import logging
from datetime import datetime

logger = logging.getLogger(__name__)

def main() -> None:
    """Run the application."""
    print(f"\nHello from app! {datetime.now()}\n")


if __name__ == "__main__":
    main()
