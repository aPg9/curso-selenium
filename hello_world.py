import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

class HelloWrold(unittest.TestCase):

    @classmethod 
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(ChromeDriverManager().install())
        driver = cls.driver
        driver.implicitly_wait(10)    
    
    def test_hello_world(self):
        driver = self.driver
        driver.get('https:www.platzi.com')

    def test_visit_wikipedia(self):
        driver = self.driver
        driver.get('https://www.google.com')    

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()
     

if __name__ == "__main__":
    unittest.main(verbosity=2, testRunner=HTMLTestRunner(output='reportes', report_name = 'hello-world-report'))        

