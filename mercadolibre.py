from time import sleep
import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

class TestingMercadoLibre(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        driver = self.driver
        driver.get('http://www.mercadolibre.com/')
        driver.maximize_window()    
    
    
    def test_search_ps4(self):
         driver = self.driver
         country = driver.find_element_by_id('CO')
         country.click()
         sleep(3)

         got_it_button = driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[2]/button[1]')
         got_it_button.click()
         sleep(2)
        

         search_field = driver.find_element_by_name('as_word')
         search_field.click()
         search_field.clear()
         search_field.send_keys('playstation 4')
         search_field.submit()
         sleep(3)

        
         location = driver.find_element_by_css_selector('#root-app > div > div > aside > form > div:nth-child(10) > ul > li:nth-child(1) > button > span.ui-search-filter-name')
         driver.execute_script("arguments[0].click();", location)         
         sleep(3)

        
         condition = driver.find_element_by_css_selector('#root-app > div > div > aside > form > div:nth-child(5) > ul > li:nth-child(1) > button > span.ui-search-filter-name')
         driver.execute_script("arguments[0].click();", condition)
         sleep(3)

        
         order_menu = driver.find_element_by_css_selector('#root-app > div > div > section > div.ui-search-view-options__container > div > div > div > div.ui-search-sort-filter > div > div > button > svg')
         order_menu.click()

         higher_price = driver.find_element_by_css_selector('#root-app > div > div > section > div.ui-search-view-options__container > div > div > div > div.ui-search-sort-filter > div > div > div > ul > a:nth-child(3) > div.andes-list__item-first-column > div.andes-list__item-text > div')
         driver.execute_script("arguments[0].click();", higher_price)
         sleep(3)
               
                
         articles = []
         prices = []


         for i in range(5):
             article_name = driver.find_element_by_xpath(f'/html/body/main/div/div/section/ol/li[{i + 1}]/div/div/div[2]/div[1]/a/h2').text
             articles.append(article_name)
             article_price = driver.find_element_by_xpath(f'/html/body/main/div/div/section/ol/li[{i + 1}]/div/div/div[2]/div[2]/div[1]/div[1]/div/div/div/span[1]/span[2]/span[2]').text
             prices.append(article_price)

         print(articles, prices)    


    
    def tearDown(self):
        self.driver.close()
     

if __name__ == "__main__":
    unittest.main(verbosity = 2) 

