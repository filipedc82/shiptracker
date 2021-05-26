from apscheduler.schedulers.blocking import BlockingScheduler
from shiptracker import scrape_ships

sched = BlockingScheduler()

sched.add_job(scrape_ships, 'interval', seconds=60)
sched.start()
