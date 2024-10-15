
from src.settings.database import ma

from src.apps.user.models import UserModel

# esto se hace para cuando se hace u query al orm poder convertilo a un formato para poder enviarlo
class UserSchema(ma.SQLAlchemyAutoSchema):
  class Meta:
    model = UserModel
