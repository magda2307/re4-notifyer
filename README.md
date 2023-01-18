# Scraping and Email Notification Script

This script is used to scrape search results for a specific keyword (Resident Evil 4) from a website (https://www.euro.com.pl/)  and send an email notification when the number of search results has increased using OAuth 2.0. This is a simple project for my girlfriend for her to be able to buy colectioner's ediiton of RE4 :)

## Prerequisites
- Python 3
- `requests`, `beautifulsoup4`, `google-auth`, `google-api-python-client`, `datetime` libraries
- Google account with access to the Google API
- OAuth 2.0 credentials for your Google account

## Setup
1. Clone the repository.
2. Install the necessary libraries.
3. Replace `youremail@gmail.com` in the script with your email address.
4. Replace `YOUR_CLIENT_ID`, `YOUR_PROJECT_ID`, `YOUR_CLIENT_SECRET` in the script with the actual values from your project's credentials.
5. Modify the script to scrape the desired website and search results for the desired keyword.
6. Run the script.

This script is set up to run indefinitely, checking for changes in the search results every 30 seconds. If the number of search results increases, an email will be sent to the provided email address.
Please note that the script uses OAuth 2.0 authentication to access the user's Gmail account and send emails.

## Error handling
In case the website structure changes or there is a pop-up on the page, the script continues working.
