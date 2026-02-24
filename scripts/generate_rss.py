import requests
from feedgen.feed import FeedGenerator
import os

REPO = "sadhugit/rancher-kb-tracker"
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
#fg.atom_link(
#    href="https://sadhugit.github.io/rancher-kb-tracker/rss.xml",
#    rel="self",
#    type="application/rss+xml")
for issue in issues:
    fe = fg.add_entry()
    fe.title(issue['title'])
    fe.link(href=issue['html_url'])
    fe.description(issue['body'])
    fe.pubDate(issue['created_at'])
    fe.guid(issue["html_url"])

fg.rss_file('rss.xml')
