from cowin_api import CoWinAPI
import json
from datetime import datetime
import smtplib


def notify_for_vaccine():
	## Email object----------------------------------------------
	smtpObj = smtplib.SMTP_SSL('smtp.gmail.com', 465)
	smtpObj.login('sender_email_id', 'password') #Put your own SMTP server Credentials
	##-----------------------------------------------------------

	## Cowin Results
	state_id = '26' #Put your state ID
	district_id = '446' #Put your disctrict ID
	date = datetime.today().strftime("%d-%m-%Y")
	min_age_limit = 18 #Put the age limit you want to register

	available_centers_data = []
	availability = 0
	cowin = CoWinAPI()

	available_centers = cowin.get_availability_by_district(district_id,date,min_age_limit)
	print("Checking centers for vaccination..........")

	for center in available_centers['centers']:
		_date_capacity = 0
		available_sessions = []

		for session in center['sessions']:
			if(session['available_capacity'] > 10): #decide availability threshold
				_date_capacity = 1
				availability = 1
				available_sessions.append(session)
		if(_date_capacity):
			center['sessions'] = available_sessions
			available_centers_data.append(center)
	## Cowin results End

	## Sending Email
	if availability == 1:
		print(json.dumps(available_centers_data))
		smtpObj.sendmail(' SMTP Sender Email ID ',
		 'xyz@gmail.com', #put recepient Email ID
		 'Subject: Covid Test Center Available!\nDear User,\
		 \n\nPlease checkout the data below for information on vaccine centers\n\n.'+
		 json.dumps(available_centers_data,indent=4)+'\n\n-----END-----')
	## -------------

	smtpObj.quit()

if __name__ == "__main__":
	notify_for_vaccine()
