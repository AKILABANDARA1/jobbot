from app.scraper import scrape_google_jobs
from app.models import SessionLocal, UserPreference
from app.matcher import match_jobs
from app.notifier import send_email
from app.utils import format_job_list

db = SessionLocal()
users = db.query(UserPreference).all()

for user in users:
    jobs = scrape_google_jobs("developer", "remote")
    matched = match_jobs({"keywords": user.keywords.split(",")}, jobs)
    if matched:
        content = format_job_list(matched)
        send_email(user.email, "New Job Matches", content)

