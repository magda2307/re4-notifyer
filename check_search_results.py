import smtplib, ssl
import requests
from bs4 import BeautifulSoup
import time
from google.oauth2.credentials import Credentials

# JSON credentials obtained from the Google API Console
creds_data = {
  "installed": {
    "client_id": "YOUR_CLIENT_ID",
    "project_id": "YOUR_PROJECT_ID",
    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
    "token_uri": "https://oauth2.googleapis.com/token",
    "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
    "client_secret": "YOUR_CLIENT_SECRET",
    "redirect_uris": [
      "urn:ietf:wg:oauth:2.0:oob",
      "http://localhost"
    ]
  }
}

creds = Credentials.from_authorized_user_info(info=creds_data)

# Email server settings
port = 465  # For SSL
smtp_server = "smtp.gmail.com"
sender_email = "youremail@gmail.com"  # Enter your address
receiver_email = "youremail@gmail.com"  # Enter receiver address

# Variable to store the previous number of search results
previous_num_results = 0

def check_search_results():
    global previous_num_results
    try:
        # URL of the search page
        url = "https://www.euro.com.pl/search.bhtml?keyword=Resident%20Evil%204"
        # Making a request to the URL
        response = requests.get(url)
        # Parsing the HTML of the response
        soup = BeautifulSoup(response.text, "html.parser")
        # Finding the div with the search results
        search_results = soup.find("div", class_="search-results").text
        # Extracting the number of results from the text
        num_results = int(search_results.split(" ")[-2])

        if num_results > previous_num_results:
            # Sending the email
            message = f"""\
            Subject: Search Results Update
            Number of search results for Resident Evil 4 has increased. The number of results is {num_results}."""
            with smtplib.SMTP_SSL(smtp_server, port, context=ssl.create_default_context()) as server:
                server.login(sender_email, creds)
                server.sendmail(sender_email, receiver_email, message)
            # Updating the previous_num_results variable
            previous_num_results = num_results
        else:
            print(f'No changes noticed. Timestamp: {datetime.now()}')
    except Exception as e:
        # In case the website structure changes or there is a pop-up on the page, the script throws an error
        print(f'An error occurred: {e}')

        
# Running the script indefinitely
while True:
    # Checking the search results
    check_search_results()
    # Waiting for 30 seconds before checking again
    time.sleep(30)
