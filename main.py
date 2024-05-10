import os
import random
import requests
from datetime import datetime
from pytz import timezone


if __name__ == "__main__":
    access_token = os.environ["GITHUB_TOKEN"]
    repository_name = os.environ["GITHUB_REPO"]
    seoul_timezone = timezone("Asia/Seoul")
    today = datetime.now(seoul_timezone)
    today_date = today.strftime("%Y년 %m월 %d일")
    headers = {
            "Authorization": f"token {access_token}",
            "Accept": "application/vnd.github.v3+json",
            "Content-Type": "application/x-www-form-urlencoded",
            }

    data = f'{{"title": "Random Number (Using Python): {random.randint(1, 1000)}"}}'

    response = requests.post(f"https://api.github.com/repos/{repository_name}/issues", headers=headers, data=data)
    print("Uploaded Random Number to Github Issue!")