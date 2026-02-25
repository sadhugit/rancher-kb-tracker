import requests
from feedgen.feed import FeedGenerator
from datetime import datetime, timezone
import os

REPO = "sadhugit/rancher-kb-tracker"
#REPO = "rancherlabs/support-kb"
TOKEN = os.getenv("GITHUB_TOKEN")
headers = {}
if TOKEN:
    headers["Authorization"] = f"token {TOKEN}"

API_URL = f"https://api.github.com/repos/{REPO}/issues?state=all&per_page=100"
response = requests.get(API_URL, headers=headers)
issues = response.json()

fg = FeedGenerator()
fg.title('Rancher KB Updates')
fg.link(href='https://github.com/sadhugit/rancher-kb-tracker')
fg.description('Latest Rancher KB Articles')
fg.link(
    href="https://sadhugit.github.io/rancher-kb-tracker/rss.xml",
    rel="self")

for issue in issues:
    fe = fg.add_entry()
    fe.title(issue['title'])
    fe.link(href=issue['html_url'])
    fe.description(issue['body'] or "No description")
    fe.published(datetime.strptime(issue['created_at'], "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=timezone.utc))
    # Entry level - use updated_at so edited/new issues surface in Slack
    fe.updated(datetime.strptime(issue['updated_at'], "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=timezone.utc))
    fe.guid(issue["html_url"], permalink=True)
    
# Feed level - tells Slack the feed was recently updated
fg.updated(datetime.now(timezone.utc))



fg.rss_file('rss.xml')
