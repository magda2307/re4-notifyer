import smtplib, ssl
import requests
from bs4 import BeautifulSoup
import time

# Function to check the search results for a specific keyword
def check_search_results():
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
    # Checking if the number of results is greater than 5
    if num_results > 5:
        send_email("Number of search results for Resident Evil 4 has increased.")
    else:
        print("Number of search results is less than or equal to 5.")

# Function to send an email
def send_email(message):
    # Email server settings
    port = 465  # For SSL
    smtp_server = "smtp.gmail.com"
    sender_email = "youremail@gmail.com"  # Enter your address
    receiver_email = "youremail@gmail.com"  # Enter receiver address
    password = "yourpassword"
    # Email message 
    message = f"""\
    Subject: Search Results Update

    {message}"""

    # Creating a SSL context
    context = ssl.create_default_context()
    # Connecting to the email server
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        # Sending the email
        server.sendmail(sender_email, receiver_email, message)

# Running the script indefinitely
while True:
    # Checking the search results
    check_search_results()
    # Waiting for 30 seconds before checking again
    time.sleep(30)
