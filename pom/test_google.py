import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from google_page import GooglePage

class GoogleTest(unittest.TestCase):
    
    @classmethod
    def setUp(cls):
        cls.driver = webdriver.Chrome(ChromeDriverManager().install())
        
    
    def test_search(self):
        google = GooglePage(self.driver)
        google.open()
        google.search('Platzi')

        self.assertEqual('Platzi', google.keyword)

    @classmethod
    def tearDown(self):
        self.driver.close()
     

if __name__ == "__main__":
    unittest.main(verbosity = 2)