import requests
from feedgen.feed import FeedGenerator

REPO = "sadhugit/rancher-kb-tracker"
API_URL = f"https://api.github.com/repos/{REPO}/issues"

response = requests.get(API_URL)
issues = response.json()

fg = FeedGenerator()
fg.title('Rancher KB Updates')
fg.link(href='https://github.com/sadhugit/rancher-kb-tracker')
fg.description('Latest Rancher KB Articles')

for issue in issues:
    fe = fg.add_entry()
    fe.title(issue['title'])
    fe.link(href=issue['html_url'])
    fe.description(issue['body'])
    fe.pubDate(issue['created_at'])

fg.rss_file('rss.xml')
