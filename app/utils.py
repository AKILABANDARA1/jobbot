def format_job_list(jobs):
    return "\n".join([f"{job['title']} - {job['company']}" for job in jobs])

