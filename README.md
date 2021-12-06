# pythonredditscraper
Reddit Web Scraper Using Python

Using the Python Reddit Scraper: 
Python is required to run this script and was written using python version 3.9.9.

Requires the following to be installed using pip: praw, pandas, numpy, and openpyxl.

(Can be done by opeing up powershell and typing in:
pip install praw
pip install pandas
pip install numpy
pip install openpyxl)

Once those have been installed. Create a folder an place the KCPopSpiderCrawler.py. (For this example I created a folder on the desktop called Reddit Scraper.)

You can run to KCPopSpiderCrawler.py in an IDE like Visual Studio Code or in Powershell by navigating to the folder in powershell and running it by typing "python .\KCPopSpiderCrawler.py"

The application will run and display the results in the terminal, but will also create two CSVs in the folder you created earlier. 

The CSV labled Formated is the best way to read the data collected. 

Code can be manipulated to scrape other subreddits. In our case we are pulling the Hot posts from the Kansas City reddit from the past week. We could change this to hot posts of today, or the year. We could even change from Hot posts to Top, New, and Rising if we wanted to.
This can be done by modifying “subs = reddit.subreddit('kansascity').hot(limit=10)” in the code. 


Known Errors:
If you run the program and have one of the excel spreadsheets that will be modified open, you will get an error letting you know to close the application and try again. 
Once the sheet is closed then the program will run like normal again. 
