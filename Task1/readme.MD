
```markdown
# GitHub Trending Repositories Scraper

This Python script utilizes the GitHub API to fetch information about trending repositories and saves it to a CSV file. It includes automation by scheduling the script to run at specific intervals using the schedule library.

## Requirements

To run this script, ensure you have Python 3 and the required libraries installed. You can install them using pip:

```bash
pip install requests
pip install pandas
pip install schedule
```

## Usage

To use this script, modify the parameters within the script to customize the search criteria based on your needs.

```python
# Set the parameters for the API request (e.g., get trending Python repositories)
params = {
    'q': 'language:python',
    'sort': 'stars',
    'order': 'desc'
}
```


Specify the time interval for running the script:

```python
# Schedule the function to run every 10 minutes
schedule.every(10).minutes.do(scrape_github_trending)
```

This example schedules the script to run every 10 minutes. You can change this interval as needed.

Run the script from the command line:

```bash
python main.py
```

The script will fetch data from the GitHub API and save it to a CSV file named "github_trending_repos.csv" in the same directory. It will also print a message indicating the status of the scraping process.

## Output

The output CSV file will contain the following columns:

- Name: Repository name
- Owner: Repository owner
- Stars: Number of stars
- Forks: Number of forks
- URL: Repository URL
- Description: Repository description

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Author
Mmamonwana Marble Tjatji <tjatjikm99@gmail.com>
```
