from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker, declarative_base

from settings import DATABASE_URL
from settings import DEBUG_SQL


engine = create_engine(DATABASE_URL,
                       connect_args={'check_same_thread': False},
                       echo=DEBUG_SQL)

SessionLocal = sessionmaker(bind=engine,
                            autocommit=False,
                            autoflush=False)


class Database:
    session: Session

    def __getattr__(self, attribute):
        return getattr(self.session, attribute)

    def __enter__(self):
        self.session = SessionLocal()
        return self

    def __exit__(self, *args):
        self.session.close()


class Model(declarative_base()):
    __abstract__ = True

    class DoesNotExist(Exception):
        pass

    @classmethod
    def insert(cls, **kwargs):
        obj = cls(**kwargs)
        with Database() as db:
            db.add(obj)
            db.commit()
            db.refresh(obj)
        return obj

    @classmethod
    def filter(cls, *criterion):
        with Database() as db:
            if result := db.query(cls).filter(*criterion):
                return result
            else:
                raise cls.DoesNotExist

    @classmethod
    def all(cls, *criterion):
        with Database() as db:
            if result := db.query(cls).all():
                return result
            else:
                raise cls.DoesNotExist

    @classmethod
    def get(cls, *criterion):
        if result := cls.filter(*criterion).first():
            return result
        else:
            raise cls.DoesNotExist

    @classmethod
    def delete(cls, *criterion):
        result = cls.filter(*criterion)
        result.delete(synchronize_session=False)
        with Database() as db:
            db.commit()


def database():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
