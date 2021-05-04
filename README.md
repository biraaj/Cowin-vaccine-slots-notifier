# Cowin-vaccine-slots-notifier
This is a simple python application to notify availability of vaccine slots in India due to competition for booking.

## Steps to install and run in local environmet.
- $git clone https://github.com/biraaj/Cowin-vaccine-slots-notifier.git
- Install all dependancies.
	- $pip install -r requirements.txt
- Run using the command below. 
	- $python cron_job.py
	
## Steps to deploy it in heroku.
- Create an account in heroku.
	- https://signup.heroku.com/
- Install heroku cli for windows or linux.
- Move to the cloned git directory.
	- $cd Cowin-vaccine-slots-notifier
- Login to heroku cli
	- $heroku login
- Create heroku application
	- $heroku create
- DO git add, commit and push to master.
	- $git add .
	- $git commit -am "First commit"
	- $git push heroku master
- Add clock in heroku.
	- $heroku ps:scale clock=1
- You can check logs at last.
	- $heroku logs --tail
- That's it you are ready with the application and you can keep checking the recepient inbox for the mail when any slot is available.

## Please do comment for suggestions.