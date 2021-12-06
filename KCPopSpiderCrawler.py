import praw
import csv
import os
import numpy as np
import sys
import openpyxl

# Log In to App:
reddit = praw.Reddit(client_id='Ftf823GXKcXaGIyVSJN0FQ', client_secret='Q7sEFCqJi_KC6dGQrRhWGLxnCCZMPA', user_agent='classwebscraper')

# Hot Submissions in the Subreddit (limit can be adjusted as preference (#.top('week')))
subs = reddit.subreddit('kansascity').hot(limit=10)

#Check for Open File and Stops if Open
try:
    if os.path.exists("Top10HotTopics.csv"):
        os.remove("Top10HotTopics.csv")
        os.remove("Formatted_Top10HotTopics.csv")
        print("% s removed previous file(s) successfully" % "Top10HotTopics & Formatted")

    #Stub Out File with Headers
    cols = ["Discussion Title","Number of Comments","Community Score","Topic URL"]
    with open('Top10HotTopics.csv', 'w') as f:
        write = csv.writer(f)
        write.writerow(cols)
        np.savetxt("Top10HotTopics.csv", cols , delimiter =',', fmt="% s")

    #Iterates through Discussion
    for submission in subs:
        print(submission.title.replace(",", ""),',',submission.num_comments,',',submission.score,',', submission.url)
        print(submission.title.replace(",", ""),',',submission.num_comments,',',submission.score,',', submission.url, file=open("Top10HotTopics.csv", "a")) 
        print("Crawl Complete")
     
    #CleanUp of Empty Rows and outputs Formatted File
    import pandas as pd
    df=pd.read_csv('Top10HotTopics.csv')
    df.to_csv('Formatted_Top10HotTopics.csv',index = False)

except OSError as error:
    print(error)
    print("*************** Please Close Previous Top10HotTopicsFile and Rerun Program ****************")

