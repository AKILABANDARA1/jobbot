def match_jobs(user_preferences, scraped_jobs):
    matched = []
    for job in scraped_jobs:
        if job['title'].lower() in user_preferences['keywords']:
            matched.append(job)
    return matched

