from django.shortcuts import render
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from django.contrib.auth.models import User
from ast import literal_eval
from .models import Dues
import os

# Create your views here.

scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']

credentials = ServiceAccountCredentials.from_json_keyfile_name(os.environ.get('CLIENT_SECRET'), scope)
# os.environ['CLIENT_SECRET']

gc = gspread.authorize(credentials)
# wks = gc.open((os.environ.get('WKS_NAME'))).sheet1
wks = gc.open((os.environ.get('WKS_NAME'))).get_worksheet(0)

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
            print(emailRow)
            d = literal_eval(str(emailRow))
            context = {
                'freshman' : d['Freshman Dues'],
                'sophomore' : d['Sophomore Dues'],
                'junior' : d['Junior Dues'],
                'senior' : d['Senior Dues'],
                'final_dues': d['Final Dues Owed'],
                'announcement' : announcement,
            }
            return render(request, 'dues/index.html', context)
