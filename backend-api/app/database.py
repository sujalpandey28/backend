from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import os
import redis


from app import initialiseenv

initialiseenv.initialise_env()

DB_DATABASE = os.environ.get("DB_DATABASE")
DB_HOST = os.environ.get("DB_HOST")
DB_PASSWORD = os.environ.get("DB_PASSWORD")
DB_USER = os.environ.get("DB_USER")
DB_PORT = os.environ.get("DB_PORT")

# redis_host = os.environ.get("REDIS_HOST")
# redis_port = os.environ.get("REDIS_PORT")
# redis_password = os.environ.get("REDIS_PASSWORD")

# Update the URL to use PostgreSQL (psycopg2 driver)
SQLALCHEMY_DATABASE_URL = (
    f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_DATABASE}"
)

# You can add SSL configuration if needed
# ssl_args = {
#     "ssl": {
#         'ssl_ca': 'ca-certificate.pem'
#     }
# }

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    # connect_args=ssl_args  # Uncomment if you need to pass SSL args
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Connecting to Redis


# redis_client = redis.Redis(host=redis_host, port=redis_port, password=redis_password)