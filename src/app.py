from flask import Flask, render_template, jsonify, request
import os 
from db import DATABASE_CONFIG
from models.modelos import db, Notifications, Area, Trainees, Evaluations, ManagersArea
template_dir = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
template_dir = os.path.join(template_dir,'src', 'templates','Page')
from sqlalchemy.exc import SQLAlchemyError
from datetime import datetime

app = Flask(__name__,template_folder=template_dir, static_folder='/' )
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://{user}:{password}@{host}/{database}'.format(
    user=DATABASE_CONFIG['user'],
    password=DATABASE_CONFIG['password'],
    host=DATABASE_CONFIG['host'],
    database=DATABASE_CONFIG['database']
)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

#Rutas de la aplicacion
@app.route('/')
def login():
    return render_template('index.html')
@app.route('/')
def main():
    return render_template('main.html')

@app.route('/IX')
def home():
    return render_template('main.html')

@app.route('/MR')
def mentores():
    return render_template('mentores.html')


@app.route('/RH')
def resorcehuman():
    return render_template('rh.html')

@app.route('/TR')
def trainee_Page():
    return render_template('trainers.html')

#Rutas endpoints 

@app.route('/BE-A01/notifications', methods=['GET'])
def get_notifications():
    try:
        
        notifications = Notifications.query.all()
        
        if not notifications:
            return jsonify({'message': 'No notifications found'}), 204
        notifications_list = []
        for notification in notifications:
            
            notifications_list.append({
                'id_Notification': notification.id_Notification,
                'area_Name': notification.area.area_Name,  # Asegúrate de tener una relación definida
                'message': notification.message,
                'notification_Date': notification.notification_Date.strftime("%Y-%m-%d %H:%M:%S")
            })
        return jsonify(notifications_list), 200
    except SQLAlchemyError as e:
        app.logger.error(f'Database error {e}')
        return jsonify({'error:' 'Internal Server Error'}),500
    
@app.route('/BE-A01/areas', methods=['GET'])
def get_areas():
    try:
        areas = Area.query.all()
        areas_list = [{'id_Area': area.id_Area, 'area_Name': area.area_Name} for area in areas]
        return jsonify(areas_list), 200
    except SQLAlchemyError as e:
        app.logger.error(f'Database error {e}')
        return jsonify({'error': 'Internal Server Error'}), 500


@app.route('/BE-A01/notifications/<int:notificationId>', methods=['GET'])
def get_notification_id(notificationId):
    try:
        notifications = Notifications.query.get_or_404(notificationId)
        result = {
            "notificationID": notifications.id_Notification,
            "area_Name":notifications.area.area_Name,
            "message": notifications.message,
            "notification_Date" : notifications.notification_Date,
        }
        return jsonify(result), 200
    except SQLAlchemyError as e:
        app.logger.error(f"Database error: {e}")
        return jsonify({'error': 'Internal Server Error'}), 500
    
########## Rutas para los post #####
    
@app.route('/BE-A01/notifications', methods=['POST'])
def add_notification():
    try:
        data = request.get_json()
        area_id = data.get('area')
        message = data.get('message')
        area = Area.query.get(area_id)

        if not area: 
            return jsonify({'error': 'Área no encontrada'}), 404
        new_notification = Notifications(
            id_Area=area_id,
            message=message,
            notification_Date= datetime.now()
        )
        
        db.session.add(new_notification)
        db.session.commit()
        created_notification = {
            'id_Notification': new_notification.id_Notification,
            'area_Name': area.area_Name,
            'message': new_notification.message,
            'notification_Date': new_notification.notification_Date.strftime("%Y-%m-%d %H:%M:%S")
        }
        return jsonify(created_notification), 201
    except SQLAlchemyError as e:
        app.logger.error(f'Error al agregar notificación: {e}')
        return jsonify({'error': 'Internal Server Error'}), 500
    



@app.route('/BE-A01/evaluations', methods=['GET'])
def get_evaluations():
    page = request.args.get('page', 1, type=int)
    page_size = request.args.get('pageSize', 10, type=int)
    evaluations = Evaluations.query.paginate(page=page, per_page=page_size).items

    result =[{
        'id_Evaluation': e.id_Evaluation,
            'id_Trainee': e.id_Trainee,
            'trainee': e.trainee,
            'task_Name': e.task_Name,
            'task_Description': e.task_Description,
            'status_task': e.status_Task,
            'feedback_Task': e.feedback_Task, 
            'quialification': e.qualifcation,
            'task_Delivery': e.task_Delivery 
    } for e in evaluations]
    return jsonify(result), 200





@app.route('/BE-A02/evaluations/<int:evaluationsId>', methods=['GET'])
def get_evaluations_id(evaluationsId):
    try:

        evaluations = Evaluations.query.get_or_404(evaluationsId)
        result = {
            
            'id_Evaluation': evaluations.id_Evaluation,
            'id_Trainee': evaluations.id_Trainee,
            'trainee': evaluations.trainee,
            'task_Name': evaluations.task_Name,
            'task_Description': evaluations.task_Description,
            'status_task': evaluations.status_Task,
            'feedback_Task': evaluations.feedback_Task, 
            'quialification': evaluations.qualifcation,
            'task_Delivery': evaluations.task_Delivery 

        }
        return jsonify(result), 200
    except SQLAlchemyError as e:
        app.logger.error(f'Database error :{e}')
        return jsonify({'error': 'Interna Server Error'}), 500


if __name__ == '__main__':
    app.run(debug=True, port=4000)