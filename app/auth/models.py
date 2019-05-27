from app import db
from app.core.models import BaseModel


class User(BaseModel):
    __tablename__ = 'auth_user'

    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username