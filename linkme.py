from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import unittest

from helper import *


""" 
******************************************************************************************************************************************
LinkMe is a super simple python script that uses Selenium to help you connect to a list of linkedIn profiles at once.
Copyright (C) 2019  Richard Iannucelli
This script is based off of Keeping-it-Green - Copyright (C) 2019  Subhajeet Mukherjee. https://github.com/bootkernel/Keeping-It-Green
This program is free software; you can redistribute it and/or
modify it under the terms of the GNU General Public License
as published by the Free Software Foundation; either version 2
of the License, or (at your option) any later version.
This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.
You should have received a copy of the GNU General Public License
along with this program; if not, write to the Free Software
Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.
******************************************************************************************************************************************
"""

# download chromedriver to local directory an enter local path below.
CHROME_DRIVER_LOCATION = r""
# LinkedIn credentials
USERNAME = ""
PASSWORD = ""

check_for_login_data(USERNAME, PASSWORD)

# get list of students
with open('students.txt') as f:
    # read, remove byte order mark from Google Docs, split, then strip.
    students = f.read().strip('ï»¿').splitlines()
    students = [x.strip() for x in students]

# get list of students that already have been sent requests.
with open("connect_req_sent.txt") as f:
    sent = f.read().splitlines()

# Remove students that have already been sent requests.
students = [x for x in students if x and x not in sent]

print(ASCII_ART)

class LinkMeBatch(unittest.TestCase):
    """Test Class to perform batch LinkedIn connection requests on your behalf."""
    def setUp(self):

        # PATH to chromedriver
        self.driver = webdriver.Chrome(CHROME_DRIVER_LOCATION)

        # Change wait_time
        self.driver.implicitly_wait(30)
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_linkme_test_case(self):
        driver = self.driver
        driver.get("https://linkedin.com/login")

        # YOUR_USERNAME in login_field
        driver.find_element_by_id("username").send_keys(USERNAME)
        driver.find_element_by_id("password").clear()

        # YOUR_PASSWORD in login_field
        driver.find_element_by_id("password").send_keys(PASSWORD)
        driver.find_element_by_css_selector("div.login__form_action_container > button[type='submit']").click()
      
        self.driver.implicitly_wait(5)

        # make sure selenium logged in.
        try:
            driver.find_element_by_id("mynetwork-nav-item")
        except NoSuchElementException as e:
            print('\n')
            print(f'Login failed. Check Username and Password!'.center(60, '*'))
            raise ValueError("Login credentials error.")

        # Send connect request to students.
        for name in students:
            driver.get(name)
            try:
                driver.find_element_by_css_selector("button.pv-s-profile-actions.pv-s-profile-actions--connect").click()
                driver.find_element_by_css_selector("div.artdeco-modal__actionbar > button[aria-label='Add a note']").click()
                driver.find_element_by_id("custom-message").send_keys(MESSAGE)
                driver.find_element_by_css_selector("div.artdeco-modal__actionbar > button[aria-label='Done']").click()
            except NoSuchElementException as e:
                print(f"\n{name} Webpage had no connect button. Selenium can't click connect.\n{e.args[0]}\n")
            
            # write name to file of requests that have already been sent.
            with open("connect_req_sent.txt", "a") as f:
                f.write(f'{name}\n')
            
        driver.close()
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)



if __name__ == "__main__":
    if students: 
        unittest.main()
    else:
        print('\n')
        print('  No new students in students list!  '.center(100, '*'))
        print('\n')
