import requests
import pandas as pd
import schedule
import time

github_api_url = "https://api.github.com/search/repositories"

def scrape_github_trending():
    params = {
        'q': 'language:python',
        'sort': 'stars',
        'order': 'desc'
    }

    response = requests.get(github_api_url, params=params)

    if response.status_code == 200:

        data = response.json()

        repo_list = data.get('items', [])
        if repo_list:
            data = []
            
            for repo in repo_list:
                
                name = repo.get("name")
                owner = repo.get("owner", {}).get("login")
                stars = repo.get("stargazers_count")
                forks = repo.get("forks_count")
                url = repo.get("html_url")
                description = repo.get("description", "No description")

                data.append([name, owner, stars, forks, url, description])

            df = pd.DataFrame(data, columns=["Name", "Owner", "Stars", "Forks", "URL", "Description"])

            print(df)

            df.to_csv("github_trending_repos.csv", index=False)
            
            print("Data scraped and saved successfully.")
        else:
            print("No trending repositories found.")
    else:
        print("Failed to scrape data. Status code:", response.status_code)

schedule.every(10).minutes.do(scrape_github_trending)

scrape_github_trending()


while True:
    schedule.run_pending()
    time.sleep(60)
