from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .settings import settings

engine = create_engine(settings.database_url, connect_args={'check_same_thread': False})


Session = sessionmaker(engine, autocommit=False, autoflush=False)


def get_session() -> Session:
    session = Session()
    try:
        yield session
    finally:
        session.close()


# from workshop.database import engine
# from workshop.tables import Base
# Base.metadata.create_all(engine)