from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import mapped_column, Mapped
from datetime import datetime, timezone
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate



db = SQLAlchemy()
migrate = Migrate()
ma = Marshmallow()


class BaseModel(db.Model):
    __abstract__ = True

    created: Mapped[datetime] = mapped_column(default=lambda: datetime.now())
    updated: Mapped[datetime] = mapped_column(default=lambda: datetime.now(), onupdate=lambda: datetime.now())

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def update(self, update_dict:dict):
        for column_name in self.__table__.columns.keys():
            if column_name in update_dict:
                setattr(self,column_name, update_dict[column_name])
        db.session.commit()

    @classmethod
    def get_all(cls):
        return cls.query.all()

def Init_database(app):
  ma.init_app(app)
  db.init_app(app)

  migrate.init_app(app,db)


