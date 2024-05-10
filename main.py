import os
import random
from datetime import datetime
from pytz import timezone
from github import Github, Auth

if __name__ == "__main__":
    access_token = os.environ['GITHUB_TOKEN']
    repository_name = "github-actions"
    seoul_timezone = timezone('Asia/Seoul')
    today = datetime.now(seoul_timezone)
    today_date = today.strftime("%Y년 %m월 %d일")
    with Github(Auth.Token(access_token)) as g:
        repo = g.get_user().get_repo(repository_name)
    repo.create_issue(title=f"Random Number (Using Python): {int(random.random()*100)}", body="")
    print("Uploaded Random Number to Github Issue!")