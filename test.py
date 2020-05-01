import unittest
from helper import check_for_login_data, url_check
from linkme import USERNAME, PASSWORD, CHROME_DRIVER_LOCATION, main


class HelperTestCase(unittest.TestCase):
    def test_check_for_login_data(self):
        self.assertEqual(check_for_login_data("x", "x", "x"), None)
        self.assertRaises(NameError, check_for_login_data, *["", "x", "x"])
        self.assertRaises(NameError, check_for_login_data, *["x", "", "x"])
        self.assertRaises(NameError, check_for_login_data, *["x", "x", ""])

    def test_url_check(self):
        result = url_check(["https://www.linkedin.com/in/q"])
        self.assertEqual(result, ["https://www.linkedin.com/in/q"])

        result = url_check(["http://www.linkedin.com/in/q"])
        self.assertEqual(result, ["https://www.linkedin.com/in/q"])

        result = url_check(["www.linkedin.com/in/q"])
        self.assertEqual(result, ["https://www.linkedin.com/in/q"])

        result = url_check(["linkedin.com/in/q"])
        self.assertEqual(result, ["https://www.linkedin.com/in/q"])

        result = url_check(["https://www.linedin.com/in/q"])
        self.assertEqual(result, [])


class LinkMeTestCase(unittest.TestCase):
    def test_check_for_empty_login_data(self):
        """Make sure login and driver data empty and main returns False."""
        self.assertEqual(USERNAME, "")
        self.assertEqual(PASSWORD, "")
        self.assertEqual(CHROME_DRIVER_LOCATION, "")
        self.assertFalse(main())

    # @unittest.skip("Uncomment this skip if necessary")
    def test_check_for_no_new_students(self):
        """
        Make sure LinkedIn is not accessed if no new students in students.txt.

        NOTE: connect_req_sent.txt must contain all links in 
        students.txt for this to pass. Skip if necessary.
        """
        self.assertFalse(main("x", "x", "x"))


if __name__ == "__main__":
    unittest.main()
