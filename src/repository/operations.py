import abc
from datetime import date, timedelta

from sqlalchemy.orm import Session

from src.repository import models


class AbstractRepository(abc.ABC):
    @abc.abstractmethod
    def add(self, model):
        raise NotImplementedError

    @abc.abstractmethod
    def get_user_by_cpf(self, cpf: str):
        raise NotImplementedError

class SqlAlchemyRepository(AbstractRepository):
    def __init__(self, session: Session):
        self._session = session()

    def add(self, model):
        self._session.add(model)
        self._session.commit()
        self._session.refresh(model)
        return model

    def get_user_by_cpf(self, cpf: str):
        return self._session.query(models.User).filter_by(cpf=cpf).one_or_none()