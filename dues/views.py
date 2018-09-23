from django.shortcuts import render
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from django.contrib.auth.models import User
from ast import literal_eval
from .models import Dues

# Create your views here.

scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']

credentials = ServiceAccountCredentials.from_json_keyfile_name('B:/client_secret.json', scope)

gc = gspread.authorize(credentials)
wks = gc.open('Class of 2021 Student E-mails and Dues').sheet1

sheet1 = wks.get_all_records()
# wks.find(user_email)                       find a string
# values_list = worksheet.col_values(1)      all values from column 1
EmailColumn = wks.col_values(1)

def index(request):
    email = request.user.email
    announcement = Dues.objects.all()
    username = request.user.username
    i = 0
    for i in range(len(EmailColumn)):
        if str(EmailColumn[i]) == email:
            emailRow = sheet1[i-1]
            d = literal_eval(str(emailRow))
            context = {
                'freshman' : d['Freshman Dues'],
                'sophomore' : d['Sophomore Dues'],
                'junior' : d['Junior Dues'],
                'senior' : d['Senior Dues'],
                'announcement' : announcement,
            }
            return render(request, 'dues/index.html', context)
