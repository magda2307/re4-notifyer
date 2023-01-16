# re4-notifyer
Very small project for my gf to track when the Resident Evil 4 Remake Collector's Edition is avaiable in Poland :) 

This script checks the number of search results for a specific keyword (resident evil 4) on a website (https://www.euro.com.pl/) and sends an email notification if the number of results increases.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

- Python 3.x
- requests library
- BeautifulSoup library
- smtplib library

### Installing

1. Clone the repository.
2. Install the required libraries
3. Update the script with your email and password, and the keyword you want to monitor
Note that you'll also need to allow "less secure apps" to connect to your account, you can follow these steps:
Go to the "Less secure app access" section in My Account.
Turn on access for less secure apps.
\The script will run indefinitely, checking the search results every 30 seconds.

## Built With

* [Python](https://www.python.org/) - The programming language used
* [requests](https://requests.readthedocs.io/en/master/) - Library used to make HTTP requests
* [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) - Library used to parse HTML
* [smtplib](https://docs.python.org/3/library/smtplib.html) - Library used to send emails

## Authors
