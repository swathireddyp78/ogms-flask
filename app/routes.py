from flask import request, flash, jsonify
from app import app, db
from werkzeug.security import generate_password_hash, check_password_hash
from app.models import Assistantship
from flask_api import status
from datetime import datetime

@app.route('/assign_assistantship',methods=['POST'])
def assign_assistantship():
    try:
        assistantship = Assistantship.query.filter_by(sid = request.json['sid']).first()
        if assistantship is None:
            assist = Assistantship(
                sid = int(request.json['sid']),
                term = request.json['term'],
                year = int(request.json['year']),
                amount = '10000'
            )
 
            db.session.add(assist)
            db.session.commit()

            return jsonify({'status': status.HTTP_201_CREATED,'message':'Assistantship awarded successfully'})
        else:
            return jsonify({'status':status.HTTP_200_OK,'message':'Student not found'})
    except Exception as e:
        return jsonify({'status': status.HTTP_500_INTERNAL_SERVER_ERROR,'message':str(e)})
        # return jsonify({'status':status.HTTP_500_INTERNAL_SERVER_ERROR,'message':'Unable to change status'})
           
@app.route('/view_fees',methods=['POST'])
def view_fees():
    try:
        sid = int(request.json['sid'])
        assistantship = Assistantship.query.filter_by(sid = sid).first()
        if assistantship is not None:
            return jsonify({'status': status.HTTP_200_OK,'amount':assistantship.amount,'message':'Assistantship awarded'})
        else:
            return jsonify({'status':status.HTTP_404_NOT_FOUND,'amount':0,'message':'No Assisstanship'})
    except Exception as e:
        return jsonify({'status': status.HTTP_500_INTERNAL_SERVER_ERROR,'message':str(e)})
        # return jsonify({'status':status.HTTP_500_INTERNAL_SERVER_ERROR,'message':'Unable to change status'})
           