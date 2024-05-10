import os
import random
from datetime import datetime
from pytz import timezone
from github import Github

if __name__ == "__main__":
    access_token = os.environ['GITHUB_TOKEN']
    repository_name = "github-actions"
    seoul_timezone = timezone('Asia/Seoul')
    today = datetime.now(seoul_timezone)
    today_date = today.strftime("%Y년 %m월 %d일")
    
    with Github(access_token) as g:
        repo = g.get_user().get_repo(repository_name)
    repo.create_issue(title=today_date, body=random.random())
    print("Uploaded Random Number to Github Issue!")

