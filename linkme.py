#!/usr/bin/env python
# linkme.py
__version__ = "0.1.1"

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import unittest
from time import sleep
import argparse
import sys

from helper import (
    check_for_login_data,
    print_no_students_txt,
    url_check,
    get_message,
    ascii_art,
    rand_sleep,
)

""" 
******************************************************************************************************************************************
LinkMe is a python script that leverages Selenium testing framework to help users grow their LinkedIn network.
If a user has a text list of LinkedIn profile URL's this script will visit each one, click the connect button, and leave a friendly message.
A list of previously visited profiles is kept and those profiles are skipped so the same source list can be run multiple times as new
names are added.
Copyright (C) 2020  Richard Iannucelli
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
# Enter correct school or group name.
SCHOOL = "Springboard"
STUDENTS = []

parser = argparse.ArgumentParser(
    description="Connect to LinkedIn profiles automatically."
)
parser.add_argument(
    "--conn-again",
    dest="conn_again",
    nargs="?",
    type=bool,
    default=False,
    const=True,
    help="Attempt to connect to profiles that had no connect button previously.",
)
args = parser.parse_args()
sys.argv[1:] = []


def main(username=USERNAME, password=PASSWORD, driver=CHROME_DRIVER_LOCATION):
    """
    Execution logic for variables setup and running 
    TestCase to interact with LinkedIn website.
    """
    ascii_art()

    try:
        check_for_login_data(username, password, driver)
    except NameError:
        return False

    # get list of students
    try:
        with open("students.txt") as f:
            # read, remove Byte order mark from Google Docs, split, then strip.
            students = f.read().strip("ï»¿").splitlines()
    except FileNotFoundError:
        print_no_students_txt()
        return False

    # make URLs conform to standard https://www.linkedin.com/in/ pattern
    students = url_check(students)

    # get list of students that already have been sent requests.
    try:
        with open("connect_req_sent.txt") as f:
            sent = [x.strip() for x in f.read().splitlines() if x]
    except FileNotFoundError:
        sent = []

    # Remove students that have already been sent requests.
    global STUDENTS
    STUDENTS = [x for x in students if x not in sent]

    # if --conn-again flag passed add no_connect_button list to STUDENTS
    # to attempt to connect to those links again.
    if args.conn_again:
        try:
            with open("no_connect_button.log") as f:
                conn_agains = [x.strip() for x in f.read().splitlines() if x]
                [STUDENTS.append(x) for x in conn_agains if x not in STUDENTS]
            with open("no_connect_button.log", "w") as f:
                f.write("")
        except FileNotFoundError:
            pass

    if STUDENTS:
        unittest.main()
    else:
        print("  No new students in students list!  ".center(100, "*"))
        print("\n")
        return False


class LinkMeBatch(unittest.TestCase):
    """Test Class to perform batch LinkedIn connection requests on your behalf."""

    def setUp(self):
        self.driver = webdriver.Chrome(CHROME_DRIVER_LOCATION)
        self.driver.implicitly_wait(30)
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_linkme_test_case(self):
        driver = self.driver
        driver.get("https://linkedin.com/login")

        # enter USERNAME
        driver.find_element_by_id("username").send_keys(USERNAME)

        # enter PASSWORD
        driver.find_element_by_id("password").send_keys(PASSWORD)
        sleep(rand_sleep(1))
        driver.find_element_by_css_selector(
            "div.login__form_action_container > button[type='submit']"
        ).click()

        self.driver.implicitly_wait(5)

        # make sure selenium logged in.
        try:
            driver.find_element_by_id("mynetwork-nav-item")
        except NoSuchElementException as e:
            print("\n")
            print(f"Login failed. Check Username and Password!".center(60, "*"))
            raise ValueError("Login credentials error.")

        # Send connect request to students.
        for link in STUDENTS:
            continue_ = True
            sleep(rand_sleep(0))
            driver.get(link)
            sleep(rand_sleep(1))

            # try to click connect
            try:
                driver.find_element_by_css_selector(
                    "button.pv-s-profile-actions.pv-s-profile-actions--connect"
                ).click()

            except NoSuchElementException as e:
                print(
                    f"\n{link} Webpage had no connect button. Selenium can't click connect.\n{e.args[0]}\n"
                )
                # if follow button present individual is out of network add to log file
                try:
                    driver.find_element_by_css_selector(
                        "button.pv-s-profile-actions--follow"
                    )
                    with open("no_connect_button.log", "a") as f:
                        f.write(f"\n{link}")
                # if no follow button this is someone you are already connected to.
                except NoSuchElementException:
                    pass
                continue_ = False

            if continue_:
                # find name and create message
                name = driver.find_element_by_css_selector(
                    "ul.pv-top-card--list.inline-flex.align-items-center > li.inline.break-words"
                ).text
                name = name.split(" ")[0]
                message = get_message(name, SCHOOL)
                sleep(1)
                # try to send message to connnect
                try:
                    driver.find_element_by_id("custom-message").send_keys(message)
                    sleep(rand_sleep(1))
                    driver.find_element_by_css_selector(
                        "div.artdeco-modal__actionbar > button[aria-label='Send invitation']"
                    ).click()
                # if no Send invitation button after clicking connect invitation is pending.
                except NoSuchElementException as e:
                    print(
                        f"\n{link} Selenium unable to send message. Connection request pending.\n{e.args[0]}\n"
                    )

            # write link to file of requests that have already been sent.
            with open("connect_req_sent.txt", "a") as f:
                f.write(f"\n{link}")

        driver.close()

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    main()
