import logging
from .app import run_application

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("/logs/app.log"),
        logging.StreamHandler()
    ]
)

if __name__ == "__main__":
    run_application()
