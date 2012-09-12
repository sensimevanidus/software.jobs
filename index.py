import web, requests

render = web.template.render("templates/")

urls = (
    '/', 'jobs'
)

app = web.application(urls, globals())

class jobs:
    def GET(self):
        jobs = requests.get("https://jobs.github.com/positions.json")
        unique_jobs = {}
        for job in jobs.json:
            if not job.get("company") in unique_jobs:
                unique_jobs[str(job.get("company"))] = []
            unique_jobs[str(job.get("company"))].append(job)
        return render.index(unique_jobs)

if __name__ == "__main__":
    app.run()
