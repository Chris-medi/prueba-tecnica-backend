
from src.settings.database import ma

from src.apps.files.models import FilesModel

# esto se hace para cuando se hace u query al orm poder convertilo a un formato para poder enviarlo
class FilesSchema(ma.SQLAlchemyAutoSchema):
  class Meta:
    model = FilesModel