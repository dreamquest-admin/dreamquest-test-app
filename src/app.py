import logging
from .database import initialize_database

logger = logging.getLogger(__name__)

def run_application():
    """Main application logic"""
    logger.info("🚀 Starting application")
    try:
        users = initialize_database()
        logger.info(f"📊 Found {len(users)} users in database")
        for user in users:
            logger.info(f"👤 User: {user[1]}, Status: {user[2]}")
    except Exception as e:
        logger.error(f"❌ Application error: {str(e)}")
        raise
    finally:
        logger.info("🏁 Application completed")
