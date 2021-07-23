from flask import Flask, request
from sqlalchemy.orm import sessionmaker

from db_connect import connection, checkout_orm, engine

app = Flask(__name__)
Session = sessionmaker(bind=engine)
session = Session()

@app.route("/health-check", methods=["GET"])
def check():
    return {"status": "OK"}

@app.route("/document-by-student-name", methods=['GET'])
def get_documetn_by_student_name():
    result = {'documents': []}
    students = session.query(checkout_orm).filter_by(name=request.form['student_name'])

    for student in students:
        student_dict = dict(student.__dict__)
        result['documents'].append(student_dict)
    
    return result

@app.route("/document-by-customer-account", methods=['GET'])
def get_document():
    result = {'documents': []}
    students = session.query(checkout_orm).filter_by(name=request.form['customer_account'])

    for student in students:
        student_dict = dict(student.__dict__)
        result['documents'].append(student_dict)
    
    return result

@app.route("/document-by-university-account", methods=['GET'])
def get_university_account():
    result = {'documents': []}
    students = session.query(checkout_orm).filter_by(name=request.form['university_account'])

    for student in students:
        student_dict = dict(student.__dict__)
        result['documents'].append(student_dict)
    
    return result

@app.route("/document-by-date", methods=['GET'])
def get_document_by_name():
    result = {'documents': []}
    students = session.query(checkout_orm).filter_by(name=request.form['date_'])

    for student in students:
        student_dict = dict(student.__dict__)
        result['documents'].append(student_dict)
    
    return result

app.run(host="0.0.0.0", port=5002)