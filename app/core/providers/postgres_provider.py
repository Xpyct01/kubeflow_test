from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from base import Base


class PostgresProvider:
    def __init__(self, config):
        database_url = config['POSTGRES_CONNECTION_STRING']
        self.engine = create_engine(database_url)
        Base.metadata.create_all(self.engine)
        self.db_session = sessionmaker(bind=self.engine)
        self.session = self.db_session()

    def get_session(self):
        return self.session
