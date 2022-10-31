# import files
from itertools import count
from multiprocessing.sharedctypes import Value
from re import X
from flask import Flask, render_template, request
import datetime
from sqlite3 import Timestamp
from fpdf import FPDF
import os

def age(birthday):
    #birthday=input("Enter Patient Brithdate? (in DD/MM/YYYY) ")  
    birthdate=datetime.datetime.strptime(birthday,"%d/%m/%Y").date()  
    today=datetime.date.today();  
    delt=today-birthdate;  
    delta=delt.days
    return delta

app = Flask(__name__)
global counter,d,file
counter=0
d=1

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/get" )
def get_bot_response():
    userText = str.lower(request.args.get('msg'))
    global w,x,y,z,d,c,customer_name,file,timestamp,report
    global counter
    if d==1:
        customer_name=userText
        d=2
       
        return str("Enter your Gender: ")
    if d==2:
        d=d+1
        return str("Enter your birthdate dd/mm/yyyy")
    if d==3:
        counter=1
        d=4
        c=age(userText)
        return str("Hi " +customer_name+" can i get the batch number")
    if userText=="0723506931" and counter==1:
        counter=2
        return str("Hello,our salaries have been delayed but hopefully will be paid today or tomorrow. Can I help you with somthing else?")
    elif (userText=="The dates of payment are still indicated n no money sent") and counter==2:
        counter=6
        return str("ok we will look into that and let you know. How can i help you?")
    elif userText=="My loan has been rejected because it was rejected recently, after 14days suspension am being suspended again for a further 7days" and counter==1:
        counter=3
        return str("We'll let you know that as soon as possible.Thanks for understanding")
    elif userText=="yes" and counter==3:
        counter=6
        return str("Patient is Lethargic. <br> <span>2)Has patient lost orientation in time and/or place?</span>")
    elif userText=="no" and counter==3:
        counter=4
        file.write("Is patient Lethargic?"+str(userText)+"\n")
        return str("Is patient Obtunded?")
    elif userText=="no" and counter==4:
        counter=5
        return str("Is patient Stuporose?")
    elif userText=='yes' and counter==4:
        counter=6
        return str("Patient is Obtunded. <br> <span>2)Has patient lost orientation in time and/or place?</span>")
    elif userText=="no" and counter==5:
        counter=6
        return str("Patient is Unconcious.<br> <span>2)Has patient lost orientation in time and/or place?</span>")
    elif userText=="no" and counter==5:
        counter=6
        return str("Patient is Stuporose.<br> <span>2)Has patient lost orientation in time and/or place?</span>")
    elif userText=='yes' and counter==6:
        counter=7
        return str("Is the confusional state acute and course fluctuating?")
    elif userText=="no" and counter==6:
        counter=11
        return str("3)How is patient's Posture? Normal/Abnormal")
    elif (userText=='yes' or userText=='no') and counter==7:
        if userText=='yes':
            w=1
        elif userText=="no":
            w=0
        counter=8
        return str("Is patient Inattentive?")
    elif (userText=='yes' or userText=='no') and counter==8:
        if userText=='yes':
            x=1
        elif userText=="no":
            x=0
        counter=9
        return str("Is patient having Disorganized thinking?")
    elif (userText=='yes' or userText=='no') and counter==9:
        if userText=='yes':
            y=1
        elif userText=="no":
            y=0
        counter=10
        return str("Does patient has altered LOC?")
    elif (userText=='yes' or userText=='no') and counter==10:
        if userText=='yes':
            z=1
        elif userText=="no":
            z=0
        a=w+x
        if a==2:
            b=a+y+z
            if b>=3:
                counter=11
                return str("Patient is in Delirium. <br><span>3)How is patient's Posture? Normal/Abnormal <span>")
        else:
            counter=11
            return str("Patient is in Confusional state. <br><span>3)How is patient's Posture? Normal/Abnormal <span>")
    elif userText=="normal" and counter==11:
        counter=16
        return str("4)Enter patient's pulse rate:")
    elif userText=="abnormal" and counter==11:
        counter=12
        return str("Restless, tossing/rolling about in bed in agony, unable to find a comfortable position? Yes / No")
    elif userText=="yes" and counter==12:
        counter=16
        return str("Patient has Colic <br><span>4)Enter patient's pulse rate:<span>")
    elif userText=="no" and counter==12:
        counter=13
        return str("Is patient more comfortable in sitting-up position?")
    elif userText=="yes" and counter==13:
        counter=16
       
        return str("Patient has either cardio-respiratory embarassment or pancreatic disorder.<br><span>4)Enter patient's pulse rate:<span>")
    elif userText=="no" and counter==13:
        counter=14
        
        return str("Does patient has fixed flexion deformity at hip joint?")
    elif userText=="yes" and counter==14:
        counter=16
        
        return str("Patient has either Iliacus heamatoma or Iliopsoas abcess.<br><span>4)Enter patient's pulse rate:<span>")
    elif userText=="no" and counter==14:
        counter=15
       
        return str("Is (The affected) Lower limb extended and externally rotated? Yes/No")
    elif userText=="yes" and counter==15:
        counter=16
      
        return str("Patient has Hemiplegia.<br><span>4)Enter patient's pulse rate:<span>")
    else:
        return str("Please give correct input")
    

if __name__ == "__main__":
    app.run()