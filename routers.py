from src.apps.user.routers import blueprint_user
from src.apps.files.routers import blueprint_files


def RegisterUSerRouter(app):
  app.register_blueprint(blueprint_user)
  app.register_blueprint(blueprint_files)

