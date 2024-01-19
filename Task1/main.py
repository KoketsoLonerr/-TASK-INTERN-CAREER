# Import the required libraries
import requests
from bs4 import BeautifulSoup
import pandas as pd
import schedule
import time

# Define the URL of the website to scrape
url = "https://www.linkedin.com/jobs/search/?keywords=software%20development"

# Define a function to scrape the data
def scrape_data(url):
    # Make a GET request to the website
    response = requests.get(url)
    # Check if the response is successful
    if response.status_code == 200:
        # Parse the HTML content using Beautiful Soup
        soup = BeautifulSoup(response.content, "html.parser")
        # Find all the job listings on the page
        jobs = soup.find_all("li", class_="result-card")
        # Create an empty list to store the scraped data
        data = []
        # Loop through each job listing
        for job in jobs:
            # Extract the job title
            title = job.find("h3", class_="result-card__title").text.strip()
            # Extract the company name
            company = job.find("h4", class_="result-card__subtitle").text.strip()
            # Extract the location
            location = job.find("span", class_="job-result-card__location").text.strip()
            # Extract the job description
            description = job.find("p", class_="job-result-card__snippet").text.strip()
            # Extract the job URL
            url = job.find("a", class_="result-card__full-card-link")["href"]
            # Append the data to the list
            data.append([title, company, location, description, url])
        # Convert the list to a pandas DataFrame
        df = pd.DataFrame(data, columns=["Title", "Company", "Location", "Description", "URL"])
        # Save the DataFrame to a CSV file
        df.to_csv("linkedin_jobs.csv", index=False)
        # Print a message
        print("Data scraped and saved successfully.")
    else:
        # Print an error message
        print("Failed to scrape data. Status code:", response.status_code)

# Schedule the function to run every day at 10:00 AM
schedule.every().day.at("10:00").do(scrape_data)

# Run the function once at the start
scrape_data(url)

# Keep the program running in a loop
while True:
    # Check if any scheduled task is pending
    schedule.run_pending()
    # Wait for one minute
    time.sleep(60)
