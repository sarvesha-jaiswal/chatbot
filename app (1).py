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

def pulse_rate(rate,delta):
    rate=int(rate)
    delta=int(delta)
    if delta<28:
        if rate>190:
            return str("Patient has Tachycardia.")
        elif rate<70:
            return str("Patient has Bradycardia.")
        else:
            return str("Patient has normal Pulse rate.")
    elif delta>=28 and delta<366:
        if rate>160:
            return str("Patient has Tachycardia.")
        elif rate<80:
            return str("Patient has Bradycardia.")
        else:
            return str("Patient has normal Pulse rate.")
    elif delta>=366 and delta<731:
        if rate>130:
            return str("Patient has Tachycardia.")
        elif rate<80:
            return str("Patient has Bradycardia.")
        else:
            return str("Patient has normal Pulse rate.")
    elif delta>=731 and delta<1826:
        if rate>120:
            return str("Patient has Tachycardia.")
        elif rate<80:
            return str("Patient has Bradycardia.")
        else:
            return str("Patient has normal Pulse rate.")
    elif delta>=1826 and delta<4381:
        if rate>110:
            return str("Patient has Tachycardia.")
        elif rate<70:
            return str("Patient has Bradycardia.")
        else:
            return str("Patient has normal Pulse rate.")
    elif delta<=4381 and delta<21536:
        if rate>80:
            return str("Patient has Tachycardia.")
        elif rate<70:
            return str("Patient has Bradycardia.")
        else:
            return str("Patient has normal Pulse rate.")
    elif delta<=21536 and delta<36501:
        if rate>70:
            return str("Patient has Tachycardia.")
        elif rate<60:
            return str("Patient has Bradycardia.")
        else:
            return str("Patient has normal Pulse rate.")

app = Flask(__name__)
global counter,d,file
counter=0
d=1
# file = open('report.txt','w+')
# file.write("Patient Details:")

@app.route("/")
def home():
    # userText = request.args.get('msg')
    # file=open("report.txt", 'w+')
    # file.write("Patient Details:")
    return render_template("index.html")


@app.route("/get" )
def get_bot_response():
    userText = str.lower(request.args.get('msg'))
    global w,x,y,z,d,c,patient_name,file,timestamp,report
    global counter
    # file.write("Patient Name-"+userText+"\n")
    # Get Patient details
    #d and counter points to next question number as per user's input and previous question number counter's value changes
    if d==1:
        patient_name=userText
        d=2
        # timestamp=str(Timestamp)
        # report=str(patient_name+timestamp)
        file = open(patient_name+'.txt','w+')
        file.write("Patient Details:")
        file.write("\nPatient Name:"+userText+"\n")
        return str("Enter patient's Gender: ")
    if d==2:
        d=d+1
        file.write("Gender: "+str(userText)+"\n")
        return str("Enter patient's birthdate dd/mm/yyyy")
    if d==3:
        counter=1
        d=4
        c=age(userText)
        file.write("Birthdate: "+str(userText)+"\n")
        # file.write("Age "+str(u))
        return str("1)Is the patient conscious (awake and alert)? ")
    if userText=="yes" and counter==1:
        counter=2
        file.write("1)Is the patient conscious (awake and alert)?"+str(userText)+"\n")
        return str("Is patient co-operative")
    elif (userText=="no" or userText=="yes") and counter==2:
        counter=6
        file.write("Is patient co-operative?"+str(userText)+"\n")
        return str("2)Has patient lost orientation in time and/or place?")
    elif userText=="no" and counter==1:
        counter=3
        file.write("1)Is the patient conscious (awake and alert)?"+str(userText)+"\n")
        return str("Is patient Lethargic?")
    elif userText=="yes" and counter==3:
        counter=6
        file.write("Is patient Lethargic?"+str(userText)+"\n")
        return str("Patient is Lethargic. <br> <span>2)Has patient lost orientation in time and/or place?</span>")
    elif userText=="no" and counter==3:
        counter=4
        file.write("Is patient Lethargic?"+str(userText)+"\n")
        return str("Is patient Obtunded?")
    elif userText=="no" and counter==4:
        counter=5
        file.write("Is patient Obtunded?"+str(userText)+"\n")
        return str("Is patient Stuporose?")
    elif userText=='yes' and counter==4:
        counter=6
        file.write("Is patient Obtunded?"+str(userText)+"\n")
        return str("Patient is Obtunded. <br> <span>2)Has patient lost orientation in time and/or place?</span>")
    elif userText=="no" and counter==5:
        counter=6
        file.write("Is patient Stuporose?"+str(userText)+"\n")
        file.write("Patient is Unconcious"+str(userText)+"\n")
        return str("Patient is Unconcious.<br> <span>2)Has patient lost orientation in time and/or place?</span>")
    elif userText=="no" and counter==5:
        counter=6
        file.write("Is patient Stuporose?"+str(userText)+"\n")
        return str("Patient is Stuporose.<br> <span>2)Has patient lost orientation in time and/or place?</span>")
    elif userText=='yes' and counter==6:
        counter=7
        file.write("2)Has patient lost orientation in time and/or place?"+str(userText)+"\n")
        return str("Is the confusional state acute and course fluctuating?")
    elif userText=="no" and counter==6:
        counter=11
        file.write("2)Has patient lost orientation in time and/or place?"+str(userText)+"\n")
        return str("3)How is patient's Posture? Normal/Abnormal")
    elif (userText=='yes' or userText=='no') and counter==7:
        if userText=='yes':
            w=1
        elif userText=="no":
            w=0
        counter=8
        # file.write("3)How is patient's Posture? Normal/Abnormal"+str(userText))
        return str("Is patient Inattentive?")
    elif (userText=='yes' or userText=='no') and counter==8:
        if userText=='yes':
            x=1
        elif userText=="no":
            x=0
        counter=9
        file.write("Is patient Inattentive?"+str(userText)+"\n")
        return str("Is patient having Disorganized thinking?")
    elif (userText=='yes' or userText=='no') and counter==9:
        if userText=='yes':
            y=1
        elif userText=="no":
            y=0
        counter=10
        file.write("Is patient having Disorganized thinking?"+str(userText)+"\n")
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
                file.write("Does patient has altered LOC?"+str(userText)+"\n")
                file.write("Patient is in Delirium \n")
                return str("Patient is in Delirium. <br><span>3)How is patient's Posture? Normal/Abnormal <span>")
        else:
            counter=11
            file.write("Does patient has altered LOC?"+str(userText)+"\n")
            file.write("Patient is in Confusional state \n")
            return str("Patient is in Confusional state. <br><span>3)How is patient's Posture? Normal/Abnormal <span>")
    elif userText=="normal" and counter==11:
        counter=16
        file.write("3)How is patient's Posture? Normal/Abnormal"+str(userText)+"\n")
        return str("4)Enter patient's pulse rate:")
    elif userText=="abnormal" and counter==11:
        counter=12
        file.write("3)How is patient's Posture? Normal/Abnormal"+str(userText)+"\n")
        return str("Restless, tossing/rolling about in bed in agony, unable to find a comfortable position? Yes / No")
    elif userText=="yes" and counter==12:
        counter=16
        file.write("Restless, tossing/rolling about in bed in agony, unable to find a comfortable position?"+str(userText)+"\n")
        return str("Patient has Colic <br><span>4)Enter patient's pulse rate:<span>")
    elif userText=="no" and counter==12:
        counter=13
        file.write("Restless, tossing/rolling about in bed in agony, unable to find a comfortable position?"+str(userText)+"\n")
        return str("Is patient more comfortable in sitting-up position?")
    elif userText=="yes" and counter==13:
        counter=16
        file.write("Is patient more comfortable in sitting-up position?"+str(userText)+"\n")
        file.write("Patient has either cardio-respiratory embarassment or pancreatic disorder\n")
        return str("Patient has either cardio-respiratory embarassment or pancreatic disorder.<br><span>4)Enter patient's pulse rate:<span>")
    elif userText=="no" and counter==13:
        counter=14
        file.write("Is patient more comfortable in sitting-up position?"+str(userText)+"\n")
        return str("Does patient has fixed flexion deformity at hip joint?")
    elif userText=="yes" and counter==14:
        counter=16
        file.write("Does patient has fixed flexion deformity at hip joint?"+str(userText)+"\n")
        return str("Patient has either Iliacus heamatoma or Iliopsoas abcess.<br><span>4)Enter patient's pulse rate:<span>")
    elif userText=="no" and counter==14:
        counter=15
        file.write("Does patient has fixed flexion deformity at hip joint?"+str(userText)+"\n")
        return str("Is (The affected) Lower limb extended and externally rotated? Yes/No")
    elif userText=="yes" and counter==15:
        counter=16
        file.write("Is (The affected) Lower limb extended and externally rotated?"+str(userText)+"\n")
        file.write("Patient has Hemiplegia\n")
        return str("Patient has Hemiplegia.<br><span>4)Enter patient's pulse rate:<span>")
    elif userText=="no" and counter==15:
        counter=16
        file.write("Is (The affected) Lower limb extended and externally rotated?"+str(userText)+"\n")
        return str("4)Enter patient's pulse rate:")
    elif counter==16:
        counter=17
        p=pulse_rate(userText,c)
        file.write("Patient's Pulse rate: "+str(userText)+"\n")
        file.write(p+"\n")
        return str(p+"<br><span>Do you want to download report?</span>")
    elif userText=="yes" and counter==17:
        file.close()
        pdf = FPDF()   
        pdf.add_page()
        pdf.set_font("Arial", size = 10)
        file = open(patient_name+".txt","r")
        for x in file: # copying conents of file in pdf
            pdf.cell(150, 10, txt = x, ln=1 , align = 'L')
        pdf.output(patient_name+".pdf")
        file.close()
        return str("<a href=\"C:\\Users\\lENOVO\\OneDrive\\Documents\\Project2\\"+patient_name+".pdf\" download=\""+patient_name+".pdf\"><button type=\"button\">Download</button></a>")
    else:
        return str("Please give correct input")
    

if __name__ == "__main__":
    app.run()