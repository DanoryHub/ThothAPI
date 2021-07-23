import sqlalchemy as db
from sqlalchemy.ext.declarative import declarative_base

config = {
    'host': 'db-service',
    'port': 3306,
    'user' :'root',
    'password': 'deeplom',
    'database': 'bntu_checkout'
}

db_user = config.get('user')
db_pwd = config.get('password')
db_host = config.get('host')
db_port = config.get('port')
db_name = config.get('database')

conn_str = f'mysql://{db_user}:{db_pwd}@{db_host}:{db_port}/{db_name}'

engine = db.create_engine(conn_str)
connection = engine.connect()

Base = declarative_base()

checkout_orm = db.Table('checkout',
    Base.metadata,
    db.Column('date_', db.String(255)),
    db.Column('customer_account', db.String(255)),
    db.Column('customer_number', db.String(255)),
    db.Column('student_name', db.String(255)),
    db.Column('university_account', db.String(255)),
    db.Column('operation_number', db.String(255)),
    db.Column('sum_', db.String(255))
)

def data_insert(**kwargs):
    """ kwargs are equal to checkout_orm columns"""
    ins = checkout_orm.insert().values(**kwargs)
    connection.execute(ins)