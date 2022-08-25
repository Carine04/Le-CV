from django.shortcuts import render
import json

def my_cv(request):

    j = open('cv_app/static/cv_app/json/mesdonnees.json','r')
    json_data = json.load(j)

    firstname = json_data.get('mydata').get('firstname')
    lastname = json_data.get('mydata').get('lastname')
    birthday = json_data.get('mydata').get('date_of_birth')
    adress = json_data.get('mydata').get('adress')
    email = json_data.get('mydata').get('email')
    phoneNumber = json_data.get('mydata').get('phoneNumber')

    context = {'firstname':firstname,'lastname':lastname,'date_of_birth':birthday,'adress':adress,'email':email,'phoneNumber':phoneNumber}

    return render(request,"cv_app/cv.html",context)