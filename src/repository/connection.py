import sqlalchemy
from sqlalchemy.orm import Session, sessionmaker

SQLALCHEMY_DATABASE_URL = "sqlite:///./authentication.db"
# SQLALCHEMY_DATABASE_URL = "postgresql://default:root@127.0.0.1:5432/cashback"

Base = sqlalchemy.orm.declarative_base()


class DatabaseConnection:
    def __new__(self) -> Session:
        self._engine = sqlalchemy.create_engine(SQLALCHEMY_DATABASE_URL)
        Base.metadata.create_all(self._engine)
        return sessionmaker(autocommit=False, autoflush=False, bind=self._engine)