
from flask import Flask, flash, render_template, request
from flask_sqlalchemy import SQLAlchemy
import datetime


from flask_wtf import FlaskForm
from wtforms import StringField,DateField,TimeField,SubmitField,EmailField,SelectField
from wtforms.validators import InputRequired

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:@localhost/app_manager'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY']="my secret key"
#Initialize the Database
db=SQLAlchemy(app)
#Create Model
class doctors(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(100), nullable=False)
    speciality=db.Column(db.String(100), nullable=False)
    y_exp=db.Column(db.Integer)

    def __repr__(self):
        return '<Name %r>'%self.name

class appointment(db.Model):
    app_id=db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name=db.Column(db.String(100), nullable=False)
    last_name=db.Column(db.String(100), nullable=False)
    mobile_no=db.Column(db.String(10), nullable=False)
    book_date=db.Column(db.String(10))
    app_date=db.Column(db.String(10))
    app_time=db.Column(db.String(10))
    email=db.Column(db.String(100))
    def __repr__(self):
        return '<Name %r>'%self.name

class AppointmentForm (FlaskForm):
    first_name =StringField("First Name:",validators=[InputRequired()])
    last_name = StringField("Last Name:",validators=[InputRequired()])
    mobile_no=StringField("Mobile No:",validators=[InputRequired()])
    email=EmailField("Email:",validators=[InputRequired()])
    book_date=DateField()
    app_date=StringField("Appointment Date:",validators=[InputRequired()])
    app_time=StringField("Appointment Time:")
    select_time=SelectField(u"Select Time:",choices=["5:00","5:10","5:20","5:30","5:40","5:50","6:00","6:10","6:20","6:30","6:40","6:50"])
    check_app=SubmitField("Check Appointment availabilty:")
    submit=SubmitField()

@app.route('/')

def home():
   our_doctors=doctors.query.order_by(doctors.id)
   return  render_template("index.html", our_doctors=our_doctors)

@app.route('/appointment', methods=['GET','POST'])

def appoint():
    # name=None
    form=AppointmentForm()
    # ch=appointment.query.filter_by(app_date=form.app_date.data).all(app_time)
    # print(ch)
    # choice=["5:00","5:10","5:20","5:30","5:40","5:50","6:00","6:10","6:20","6:30","6:40","6:50"]-ch
    # form.select_time=SelectField(u"Select Time:",choices=["5:40","5:50","6:00","6:10","6:20","6:30","6:40","6:50"])
    valid=form.validate_on_submit()
    # print(valid)
    if valid :
        user=appointment(first_name=form.first_name.data,last_name=form.last_name.data,
        mobile_no=form.mobile_no.data,book_date=datetime.datetime.utcnow(),email=form.email.data,app_date=form.app_date.data,app_time=form.select_time.data)
        db.session.add(user)
        db.session.commit()
        form.first_name.data=" "
        form.last_name.data=" "
        form.mobile_no.data=" "
        form.email.data=" "
        form.app_date.data=" "
        flash("Appointment Booked")
    appointment_now=appointment.query.all()
    return  render_template("appointment.html",form=form,appointment_now=appointment_now)

if __name__ == "__main__":
    app.run()
