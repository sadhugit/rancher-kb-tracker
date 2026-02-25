🚀 **rancher-kb-tracker**


A lightweight, automated tracker that monitors Rancher Knowledge Base (KB) GitHub issues and generates a live RSS feed for updates.

Stay informed whenever a new KB article is created or an existing one is updated without manually checking GitHub.


📖 **Overview**
Many critical technical solutions for Rancher are documented as GitHub issues in specific repositories. rancher-kb-tracker automates the process of "watching" these articles by:

Monitoring the creation and modification of issues.

Generate a valid RSS feed containing these updates.

Enabling users to subscribe via their favorite RSS reader (Slack, Outlook, Feedly, etc.) to get instant notifications.


✨ **Features**
Real-time Tracking: Captures new issues (New KBs) and existing issue updates (Updated KBs).

Automated Updates: Powered by GitHub Actions—no manual server maintenance required.

RSS Notifications: Easily integrate with notification tools like Slack, Microsoft Teams, or Discord.

Public Visibility: Hosted on GitHub Pages or directly in the repo for easy access to the feed URL.


🛠 **How It Works**


This project uses a GitHub Workflow to scan the target Rancher repository issues for specific events(open/update)
Trigger: The workflow runs on a specific action

Process: It fetches issue data, filters for relevant labels/titles, and formats the metadata into an XML/RSS file.

Deploy: The updated feed is committed back to the repository.



🚀 **Getting Started**

1. Subscribe to the Feed
Copy the link to the generated rss.xml file and paste it into your RSS reader:
```https://sadhugit.github.io/rancher-kb-tracker/rss.xml```



2. Fork & Customize

   
If you want to track a different set of issues:

Fork this repository: ```sadhugit/rancher-kb-tracker```.

Update the ```.github/workflows/rss.yml``` with your target repository URL.

Enable GitHub Actions in your settings tab.



📂 **Project Structure**
Bash
```
.
├── .github/workflows/rss.yml # Automation logic to install required packages and call python script.
├── scripts/                  # Script to parse issues and generate RSS
├── rss.xml                   # The live RSS feed (auto-generated)
└── README.md                 # Project documentation
└── index.html                # to auto-detect RSS feed
└── requirements.txt          # To specify the required dependent packages

```



🤝 Contributing
Contributions are welcome! If you have ideas for better filtering or new notification channels, feel free to:

1. Open an Issue.

2. Submit a Pull Request.
