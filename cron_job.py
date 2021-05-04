# Package Scheduler.
from apscheduler.schedulers.blocking import BlockingScheduler

# Main cronjob function.
from vaccine_tracker import notify_for_vaccine

# Create an instance of scheduler and add function.
scheduler = BlockingScheduler()
scheduler.add_job(notify_for_vaccine, "interval", seconds=1800) #Put the intervals as per desired frequency to check and notify in seconds.
print("cron job is scheduled")
scheduler.start()