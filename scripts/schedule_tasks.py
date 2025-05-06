import schedule
import time
import subprocess

schedule.every(6).hours.do(lambda: subprocess.run(["python", "scripts/run_scraper.py"]))

while True:
    schedule.run_pending()
    time.sleep(60)

