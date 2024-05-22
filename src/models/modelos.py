from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
from datetime import datetime
db = SQLAlchemy()

class Area(db.Model):
    __tablename__='area'
    id_Area= db.Column(db.Integer, primary_key=True, autoincrement=True)
    area_Name = db.Column(db.String(100),unique=True, nullable=False)

class Trainees(db.Model):
    __tablename__='trainees'
    id_Trainee = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_Leader = db.Column(db.Integer, db.ForeignKey('leaders.id_Leader'))
    leader = db.relationship('Leaders', backref='trainees')
    id_Area = db.Column(db.Integer, db.ForeignKey('area.id_Area'))
    area = db.relationship('Area', backref='trainees')
    employee_Number = db.Column(db.Integer)
    trainee_Name = db.Column(db.String(150), nullable=False)
    trainee_Area = db.Column(db.String(100), nullable=False)
    email_Trainee = db.Column(db.String(65), nullable=False)
    phone_Trainee = db.Column(db.String(13))
    date_Start_Trainee = db.Column(db.DateTime, nullable=False, default=datetime.now())
    
    

class Leaders(db.Model):
    __tablename__='leaders'
    id_Leader = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_Area = db.Column(db.Integer, db.ForeignKey('area.id_Area'))
    area = db.relationship('Area', backref='leaders')
    leader_Name= db.Column(db.String(150), nullable=False)
    position_Leader= db.Column(db.String(100), nullable=False)
    email_Leader = db.Column(db.String(65), nullable=False)
    phone_Leader = db.Column(db.String(13), nullable=False)
    

class Evaluations(db.Model):
    __tablename__='evaluation'
    id_Evaluation = db.Column(db.Integer, primary_key=True,autoincrement=True)
    id_Trainee = db.Column(db.Integer, db.ForeignKey('trainees.id_Trainee'))
    trainee = db.relationship('Trainees', backref='evaluations')
    task_Name = db.Column(db.String(50), nullable=False)
    task_Description= db.Column(db.String(150), nullable=False)
    status_Task = db.Column(db.Boolean, default=False)
    feedback_Task = db.Column(db.String(150))
    qualifcation= db.Column(db.Integer)
    task_Delivery = db.Column(db.DateTime, nullable=False, default=datetime.now())
    


class Notifications(db.Model):
    __tablename__='notifications'
    id_Notification = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_Area = db.Column(db.Integer, db.ForeignKey('area.id_Area'))
    area = db.relationship('Area', backref='notifications')
    message = db.Column(db.String(250))
    notification_Date = db.Column(db.DateTime, nullable=False, default=datetime.now())
    


class ManagersArea(db.Model):
    __tablename__='managersArea'
    id_Manager = db.Column(db.Integer, primary_key = True, autoincrement=True)
    id_Area = db.Column(db.Integer, db.ForeignKey('area.id_Area'))
    areaManager = db.relationship('Area', backref='managers_Area')
    manager_Name = db.Column(db.String(150), nullable= False)
    position_Manager = db.Column(db.String(100), nullable=False)
    email_Manager = db.Column(db.String(65), nullable=False)
    phone_Manager = db.Column(db.String(13), nullable=False)
    
    



