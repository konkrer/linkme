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
        out = url_check(["https://www.linkedin.com/in/q"])
        self.assertEqual(out, ["https://www.linkedin.com/in/q"])

        out = url_check(["http://www.linkedin.com/in/q"])
        self.assertEqual(out, ["https://www.linkedin.com/in/q"])

        out = url_check(["www.linkedin.com/in/q"])
        self.assertEqual(out, ["https://www.linkedin.com/in/q"])

        out = url_check(["linkedin.com/in/q"])
        self.assertEqual(out, ["https://www.linkedin.com/in/q"])

        out = url_check(["https://www.linedin.com/in/q"])
        self.assertEqual(out, [])


class LinkMeTestCase(unittest.TestCase):
    def test_check_for_empty_login_data(self):
        """Make sure login and driver data empty and error raised."""
        self.assertEqual(USERNAME, "")
        self.assertEqual(PASSWORD, "")
        self.assertEqual(CHROME_DRIVER_LOCATION, "")
        self.assertRaises(NameError, main)

    # @unittest.skip("Uncomment this skip if necesarry")
    def test_check_for_no_new_students(self):
        """
        Sent list must contain all links in 
        students.txt for this to pass.
        """
        self.assertFalse(main("x", "x", "x"))


if __name__ == "__main__":
    unittest.main()
