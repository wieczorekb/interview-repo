import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

@pytest.mark.usefixtures("setUp")


class Test_JobOffersList:


    def test_Canada_Offers(self):

        # locators to test Canada offers
        TAB_CAREERS = "//div[@id='main-navbar']//a[@href='/en/careers']"
        DDN_ROLES_LOCATIONS = "//*[@id='main-navbar']//a[@href='/en/careers/roles-and-locations']"
        TAB_SEARCH = "//a[@href='#search-jobs']"
        TXT_SEARCH = "//input[@id='tpt_search']"
        BTN_SEARCH = "//button[@value='search']"
        BTN_NEXT = "//span[@class ='nextLink']"



        tabCareers = self.driver.find_element(By.XPATH, TAB_CAREERS)
        tabCareersHov = ActionChains(self.driver).move_to_element(tabCareers)
        tabCareersHov.perform()

        # wait until career drop-down option is visible and click on it
        ddnRlesLocations = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, DDN_ROLES_LOCATIONS)))
        ddnRlesLocations.click()

        # Click on TAB_SEARCH
        self.driver.execute_script("window.scrollBy(0, 200);")
        searchJobs = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, TAB_SEARCH)))
        searchJobs.click()

        # Search for Canada offers
        txtSearch = self.driver.find_element(By.XPATH, TXT_SEARCH)
        txtSearch.send_keys('Canada')

        # Click on Search button
        self.driver.find_element(By.XPATH, BTN_SEARCH).click()
        time.sleep(3)

        # scroll down
        self.driver.execute_script("window.scrollBy(0, 1000);")
        time.sleep(3)
        # Check if BTN_NEXT is displayed. When btn is not available, then there is only one page of results for Canada
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, BTN_NEXT)))
            btnNextNotFound = False

        except:
            btnNextNotFound = True

        assert btnNextNotFound, 'Result: FAIL, There is NOT only 1 page of results'

    def test_Denmark_Offers(self):

        TXT_SEARCH = "//input[@id='tpt_search']"
        BTN_SEARCH = "//button[@value='search']"
        LNK_JOB_OFFER = "// div[@class ='listJobs']//li[1]"

        # scroll up
        self.driver.execute_script("window.scrollBy(0, -1000);")
        time.sleep(3)

        # clear search field and type: Denmark
        txtSearch = self.driver.find_element(By.XPATH, TXT_SEARCH)
        txtSearch.clear()
        txtSearch.send_keys('Denmark')
        time.sleep(5)

        # Click on Search button
        self.driver.find_element(By.XPATH, BTN_SEARCH).click()
        # Assertion - at list one search result, when this element is visible
        jobOffer = self.driver.find_element(By.XPATH, LNK_JOB_OFFER).is_displayed()
        assert jobOffer == True, 'No job offer is visible on the page'

ff=Test_JobOffersList
ff()

