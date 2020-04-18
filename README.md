# LinkMe LinkedIn Connection Automation Tool

This command-line Python tool automates the process of logging into LinkedIn
and submitting "Connect" to a list of LinkedIn profile URLs. This tool is
intended for students and the like who wish to grow their network from a list
of fellow students also looking to connect. A text document such as a Google
Docs file can hold the list of LinkedIn profile URLs and is downloaded to the
project folder for the script to use.

## Quick Start 

1. Install Python.
2. Clone repository.
3. Create a virtual environment and install selenium.
4. Download chromedriver to local project directory for selenium to use.
5. Set CHROME_DRIVER_LOCATION in linkme.py to the relative path to the chromedriver 
   file (i.e. chromedriver.exe).
6. Set USERNAME and PASSWORD in linkme.py for your LinkedIn account.
7. Download a text file of LinkedIn profile URL's and save as students.txt
   (overwrite old file).
8. Run the script: python linkme.py
9. Enjoy your new LinkedIn connections!


### Note on chromedriver:

Go to https://sites.google.com/a/chromium.org/chromedriver/downloads and download
chromedriver for the version of Chrome you use. Unzip file and place in project 
folder and set CHROME_DRIVER_LOCATION to the local path to the driver file.

In my setup, for example, I left the driver in the folder it was originally in
and set my CHROME_DRIVER_LOCATION = r"chromedriver_win32\chromedriver.exe".



![LinkMe logo](https://repository-images.githubusercontent.com/256674880/e5de8900-80f9-11ea-9ff4-3c3b16893bb9)
