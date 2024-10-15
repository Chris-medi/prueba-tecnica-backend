from flask_jwt_extended import jwt_required
from flask import request, url_for, Blueprint, jsonify
from sqlalchemy.exc import IntegrityError

from src.apps.files.schemas import FilesSchema
from src.apps.files.models import FilesModel
from src.settings.config import Config

import os

from src.settings.config import Config

blueprint_files = Blueprint('files_api', __name__,url_prefix=Config.APPLICATION_ROOT)

@blueprint_files.route('/files', methods=['POST','GET','DELETE','PUT'])
def CreateFile():
  if request.method == 'POST':
    try:
      file = request.files["file"]
      extension = file.filename.split('.')[-1]
      file_name = request.form['file_name'].split('.')[:-1]
      file_name = ''.join(file_name)
      file_name = f'{file_name}.{extension}'
      file.save(f'static/{file_name}')
      url = str(url_for('static', filename=file_name,_external=True))
      row = FilesModel(last_name=request.form['last_name'],documento=request.form['documento'],name=request.form['name'],file_path=url)
      row.save()
    except IntegrityError:
      return jsonify({'msg':'Error en la base de datos'}), 303
    except Exception as e:
      print(e)
      return jsonify({'msg':'Error el el servidor'}), 400
    return jsonify({'msg':'Archivo creado exitosamente' }), 200

  elif request.method == 'DELETE':
    try:
      row = FilesModel.query.filter_by(id=request.get_json()['id']).first()
      os.remove(f'static/{row.file_path.split('/')[-1]}')
      row.delete()
    except Exception as e:
      print(e)
      return jsonify({'msg':'Error el el servidor'}), 400
    return jsonify({'msg':'Archivo eliminado exitosamente' }), 200
  elif request.method == 'PUT':
    try:
      row = FilesModel.query.filter_by(id=request.form['id']).first()
      json = request.form.to_dict()
      if len(request.files) > 0:
        file_name = row.file_path.split('/')[-1]
        file_path = f'static/{file_name}'
        os.remove(file_path)

        file = request.files["file"]
        file.save(f'static/{file.filename}')

        url = str(url_for('static', filename=file.filename,_external=True))
        json['file_path'] = url

      row.update(json)
      return jsonify({'msg':'archivo actualizado exitosamente'}),200
    except Exception as e:
      print(e)
      return jsonify({'msg':'Error en el servidor'}), 500


  else:
    files = FilesSchema(many=True).dump(FilesModel.query.all())
    return jsonify({'msg': 'all files', 'data': files}), 200




