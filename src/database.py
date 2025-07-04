import psycopg2
import os
import logging

logger = logging.getLogger(__name__)

def get_db_connection():
    """Create and return database connection"""
    return psycopg2.connect(
        host=os.getenv("DB_HOST"),
        database=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        port=os.getenv("DB_PORT", "5432")
    )

def initialize_database():
    """Create table and insert test user"""
    conn = get_db_connection()
    try:
        with conn.cursor() as cur:
            # Create USERS table
            cur.execute("""
                CREATE TABLE IF NOT EXISTS users (
                    id SERIAL PRIMARY KEY,
                    username VARCHAR(50) UNIQUE NOT NULL,
                    status VARCHAR(20) NOT NULL,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            """)
            
            # Insert test user
            cur.execute("""
                INSERT INTO users (username, status)
                VALUES ('test', 'Active')
                ON CONFLICT (username) DO NOTHING
            """)
            
            # Fetch all users
            cur.execute("SELECT * FROM users")
            users = cur.fetchall()
            
            logger.info("✅ Database initialized successfully")
            return users
    finally:
        conn.commit()
        conn.close()
