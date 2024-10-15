from flask_jwt_extended import create_access_token
from flask import request, url_for, redirect
from sqlalchemy.exc import IntegrityError
import secrets

from src.settings.database import db
from src.apps.user.schemas import UserSchema
from src.apps.user.models import UserModel
from src.settings.config import Config
from src.settings.oauth import oauth

from src.apps.user.utils import sendEmail

from flask import Blueprint, jsonify

blueprint_user = Blueprint('user_api', __name__,url_prefix=Config.APPLICATION_ROOT)

@blueprint_user.route('/user', methods=['POST'])
def CreateUser():
    try:
      UserModel(name=request.json['name']).save()
    except IntegrityError:
      return jsonify({'msg':'Error el usuario ya existe'}), 303
    except Exception as e:
      print(e)
      return jsonify({'msg':'Error el el servidor'}), 400
    return jsonify({'msg':'usuario creado exitosamente'}), 201


@blueprint_user.route('/session', methods=['POST'])
def session():
  email = request.json['correo']
  row = UserModel.query.filter_by(email=email).first()
  code_to_login = str(secrets.token_urlsafe(6))
  try:
    if not row :
      UserModel(email=email,code_to_login=code_to_login).save()
      row = UserModel.query.filter_by(email=email).first()

    row.update({'code_to_login': code_to_login})
    sendEmail(row.email, code_to_login)

    return jsonify({'msg': 'usuaio creado con exito'}), 200

  except Exception as e:
    return jsonify({'msg': 'Error el servidor'}), 500
    # crear usuario

@blueprint_user.route('/validate', methods=['POST'])
def validate():
  email = request.json['correo']
  code = request.json['code']
  row = UserModel.query.filter_by(email=email).first()
  token = create_access_token(identity=email)
  if code == row.code_to_login:
    return jsonify({'msg': 'token de validacacion', 'token': token }), 200

  return jsonify({'msg': 'codigo incorrecto'}), 403


@blueprint_user.route('/login')
def login():
  redirect_uri = url_for('user_api.auth',_external=True)
  return oauth.google.authorize_redirect(redirect_uri)

@blueprint_user.route('/auth')
def auth():
  token = oauth.google.authorize_access_token()
  print(token)
  return redirect('/')

